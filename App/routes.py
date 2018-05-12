import json, os, datetime
from functools import wraps
from flask import render_template, request, flash, redirect, url_for, make_response, session, jsonify
from werkzeug.utils import secure_filename
from . import app, allowed_file, read_file
from App  import dbconnect
from App.forms import *

try:
	CONN, CURSOR = dbconnect.connection()
except Exception as e:
	print(e)
	exit()

def user_login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if 'mainPage' not in session or session['mainPage'] != '/dashboard':
			flash('Login to access user pages.')
			return redirect(url_for('index'))
		return f(*args, **kwargs)
	return decorated_function

def admin_login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if 'mainPage' not in session or session['mainPage'] != '/admin':
			flash('Admin login required to complete the request.')
			return redirect(url_for('index'))
		return f(*args, **kwargs)
	return decorated_function

@app.route('/', methods=['GET', 'POST'])
def index():
	loginForm = LoginForm(request.form)
	if request.method == 'POST':
		if loginForm.validate_on_submit():
			if loginForm.accType.data == 'FlatAcc':
				return redirect(url_for('userDashboard'))
			else:
				return redirect(url_for('adminPage'))
				#to-do: REDIRECT TO ADMIN PAGE
		else:
			for error in loginForm.errors.values():
				flash(str(error[0]))

	return render_template('index.html', form=loginForm)

@app.route('/admin', methods=['GET'])
@admin_login_required
def adminPage():
	addressQuery = "SELECT * FROM society WHERE society_id=%d" % (session['societyId'])
	CURSOR.execute(addressQuery)
	addressRes = CURSOR.fetchone()
	address = [str(addressRes[2]), str(addressRes[3]), str(addressRes[4]), str(addressRes[5])]
	address = ', '.join(address) + '.'

	statsCounter = {'residents': 0, 'flats':0, 'wings': 0, 'admins':0}

	wingsQuery = "SELECT wing_id FROM wing WHERE society_id=%d" % (session['societyId'])
	CURSOR.execute(wingsQuery)
	wings = CURSOR.fetchall()
	statsCounter['wings'] = len(wings)
	flats = []
	if statsCounter['wings'] > 0:
		flatsQuery = "SELECT flat_id FROM flat WHERE wing_id in (%s)" % (','.join([str(x[0]) for x in wings]))
		CURSOR.execute(flatsQuery)
		flats = CURSOR.fetchall()
		statsCounter['flats'] = len(flats)

	if len(flats) > 0:
		residentsQuery = "SELECT COUNT(resident_id) FROM resident WHERE flat_id IN (%s)" % (','.join([str(x[0]) for x in flats]))
		CURSOR.execute(residentsQuery)
		statsCounter['residents'] = CURSOR.fetchone()[0]

	adminCountQuery = "SELECT COUNT(resident_id) FROM admin WHERE society_id=%d" % (session['societyId'])
	CURSOR.execute(adminCountQuery)
	statsCounter['admins'] = CURSOR.fetchone()[0]
	
	newNoticeForm = AddNoticeForm (request.form)
	newBillForm   = AddBillForm   (request.form)

	return render_template('admin/adminpage.html', address=address, counter=statsCounter, noticeForm=newNoticeForm, billForm=newBillForm)

@app.route('/addNotice', methods=['POST'])
@admin_login_required
def addNotice():
	submittedNotice = AddNoticeForm(request.form)

	if submittedNotice.validate_on_submit():
		flash('Added Notice')
	flash('Error Notice')
	return redirect(url_for('adminPage'))

@app.route('/addBill', methods=['POST'])
@admin_login_required
def addBill():
	submittedBill = AddBillForm(request.form)

	if submittedBill.validate_on_submit():
		flash('Added bill')
	flash('Error bill')

	return redirect(url_for('adminPage'))


@app.route('/logout', methods=['GET'])
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/refreshNotices', methods=['GET'])
@user_login_required
def getNoticeList():

	noticeQuery = "SELECT * FROM notices \
					WHERE notice_id in (SELECT notice_id FROM flat_addr WHERE flat_id=%d)" % (session['flatId'])
	CURSOR.execute(noticeQuery)

	result = CURSOR.fetchall()
	noticeList = [{'subject':row[2], 'date':str(row[3]), 'body':row[4]} for row in result]
	
	noticeList = json.dumps(noticeList)
	return noticeList


@app.route('/dashboard', methods=['GET'])
@user_login_required
def userDashboard():
	return render_template('user/userdashboard.html')

@app.route('/bills')
@user_login_required
def userBill():
	categories = {'WATER CHARGES':3, 'PROPERTY TAX':4, 'ELECTRICITY CHARGES':5, 'SINKING FUNDS':6, 'PARKING CHARGES':7, 'NOC':8, 'INSURANCE':9, 'OTHER':10}

	billListQuery = "SELECT due_date, amount, bill_num \
					FROM maintenance_bill \
					WHERE flat_id='%d'\
					ORDER BY due_date DESC" % (session['flatId'])

	CURSOR.execute(billListQuery)
	billList = CURSOR.fetchall()
	latest_bill = billList[0]
	billList = [{'date': bill[0], 'amount': bill[1]} for bill in billList]

	if len(billList) <= 0:
		currBill = {}
		currBill['date']    = 'N.A.'
		currBill['entries'] = [{'category': x, 'cost': 0} for x in categories]
		currBill['amount']  = 0
		return render_template('user/userbillpage.html', currBill=currBill, billList=billList)


	if len(request.args) <= 0:
		currBillQuery = "SELECT * FROM maintenance_bill WHERE bill_num=%d" % (latest_bill[2])
	else:
		day   = request.args.get('dd')
		month = request.args.get('mm')
		year  = request.args.get('yyyy')
		
		billDate      = '-'.join((year, month, day))
		currBillQuery = "SELECT * FROM maintenance_bill WHERE due_date='%s'" % (billDate)


	CURSOR.execute(currBillQuery)
	currBillResult = CURSOR.fetchone()
	currBill = {}
	currBill['date'] = currBillResult[11]
	currBill['entries'] = [ { 'category' : x, 'cost' : float(currBillResult[categories[x]])} for x in categories]
	currBill['amount'] = currBillResult[12]

	print(currBill['entries'])
	return render_template('user/userbillpage.html', currBill=currBill, billList=billList)

@app.route('/profile')
@user_login_required
def userProfile():
		ownerNameQuery = "SELECT owner_name, pending_dues, profile_img FROM account WHERE acc_name='%s'" % (session['accName'])
		CURSOR.execute(ownerNameQuery)
		ownerRes    = CURSOR.fetchone()
		ownerName   = ownerRes[0]
		pendingDues = ownerRes[1]
		profImage   = ownerRes[2]

		print(profImage)

		residentQuery = "SELECT resident_name, resident_id FROM resident WHERE flat_id=%d" % (session['flatId'])
		CURSOR.execute(residentQuery)

		resList = [{'name' :row[0], 'phone': str(1234), 'id': str(row[1])} for row in CURSOR.fetchall()]

		return render_template('user/userprofile.html', ownerName = ownerName, resList = resList, pendingDues = pendingDues)

@app.route('/editDetails', methods=['POST'])
@user_login_required
def updateUserDetails():
	#DO ALL DATABASE UPDATES HERE
	for key in request.form.keys():
		print(key)
        # print("Hello")
        # new_owner=request.form['NameRes1']
        # new_contact=int(request.form['NumRes1'])
        # print(new_owner)
        # print(new_contact)
        # check_present_query = "SELECT resident_id, contact FROM resident WHERE resident_name='%s' AND flat_id=%d" % (new_owner, session['flatId'])
        # CURSOR.execute(check_present_query)
        # if(CURSOR.rowcount <= 0):
        #     check_max_query = "SELECT MAX(resident_id) FROM resident"
        #     CURSOR.execute(check_max_query)
        #     curr_max = CURSOR.fetchone()
        #     new_max = curr_max[0] + 1
        #     print(new_max)
        #     #new_res_query = "INSERT INTO resident VALUES(%d, %d, '%s', %d)" % (new_max, session['flatId'], new_owner, new_contact)
        #     #CURSOR.execute(new_res_query)
        #     CURSOR.execute("INSERT INTO resident VALUES(%s, %s, %s, %s)", [int(new_max), int(session['flatId']), new_owner, new_contact])
        #     CONN.commit()
        # else:
        #     r = CURSOR.fetchone()
        #     res_id = r[0]
        #     old_contact = r[1]
        #     if(new_contact != old_contact):
        #         new_cont_query = "UPDATE resident SET contact=%d WHERE resident_id=%d" % (new_contact, res_id) 
        #         CURSOR.execute(new_cont_query)
        #         CONN.commit()
	return redirect(url_for('userProfile'))

@app.route('/issues', methods=['GET', 'POST'])
@user_login_required
def getComplaints():
	#get the POST DATA from forms if submitted
	if(request.method == 'POST'):
		related = request.form.get("relatedTo", None)
		if(related == None):
			related = 'None'
		print(related)
		complaint = request.form['complaints']
		print(complaint)
		accId = session['accName']
		now = datetime.datetime.now()
		curr_year = str(now.year)
		if(now.month < 10):
			curr_month = '0' + str(now.month)
		else:
			curr_month = str(now.month)
		if(now.day < 10):
			curr_day = '0' + str(now.day)
		else:
			curr_day = str(now.day)
		curr_date = curr_year + curr_month + curr_day
		print(accId)
		print(curr_date)
		check_max_query = "SELECT MAX(issue_id) FROM issues"
		CURSOR.execute(check_max_query)
		curr_max = CURSOR.fetchone()
		print(curr_max)
		if curr_max[0] is not None:
			new_max = curr_max[0] + 1
			print(new_max)
            #new_issue_query = "INSERT INTO issues VALUES(%d, %d, '%s', '%s', '', '%s')" % (new_max, accId, curr_date, complaint, related)
            #CURSOR.execute(new_issue_query)
			CURSOR.execute("INSERT INTO issues VALUES(%s, %s, %s, %s, '', %s)", [int(new_max), int(accId), curr_date, complaint, related])
			CONN.commit()
		return redirect(url_for('getComplaints'))

	elif(request.method == 'GET'):
		issuesQuery = "SELECT issue_date, issue_desc, related FROM issues WHERE acc_name IN (SELECT acc_name FROM account WHERE flat_id=%d) ORDER BY issue_date" % (session['flatId'])
		CURSOR.execute(issuesQuery)

		issuesList = [{'date': str(row[0]), 'desc': row[1], 'related': row[2]} for row in CURSOR.fetchall()]

		return render_template('user/usercomplaints.html', issuesList = issuesList)


@app.route('/editProfileImage', methods=['POST'])
@user_login_required
def uploadProfileImage():
	if 'profImage' in request.files:
		profImage = request.files['profImage']

		if profImage and allowed_file(profImage.filename):
			profImage = profImage.read()

			removeOldProfFileQuery = 'UPDATE account SET profile_img=NULL WHERE acc_name="%s"' % (session['accName'])
			CURSOR.execute(removeOldProfFileQuery)

			uploadProfFileQuery = 'UPDATE account SET profile_img=%s WHERE acc_name="%s"' % (profImage, session['accName'])
			CURSOR.execute(uploadProfFileQuery)
		else:
			flash('Invalid file format.')
			#image = read_file(profImage)
			#print(os.path.join(app.config['UPLOAD_FOLDER'], session['societyName'], 'images', profFileName))


	else:
		flash('Invalid / Empty file uploaded. Try again')

	return redirect(url_for('userProfile'))