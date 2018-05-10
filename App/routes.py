import json, os, datetime
from flask import render_template, request, flash, redirect, url_for, make_response, session, jsonify
from werkzeug.utils import secure_filename
from . import app, allowed_file
from App  import dbconnect
from App.forms import *

try:
	CONN, CURSOR = dbconnect.connection()
except Exception as e:
	print(e)
	exit()

@app.route('/', methods=['GET', 'POST'])
def index():
	loginForm = LoginForm(request.form)
	if request.method == 'POST':
		if loginForm.validate_on_submit():
			if loginForm.accType.data == 'FlatAcc':
				return redirect(url_for('userDashboard'))
			else:
				pass
				#to-do: REDIRECT TO ADMIN PAGE
		else:
			for error in loginForm.errors.values():
				flash(str(error[0]))

	return render_template('index.html', form=loginForm)

@app.route('/admin', methods=['GET'])
def adminPage():
	return render_template('admin/adminpage.html')

@app.route('/logout', methods=['GET'])
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/refreshNotices', methods=['GET'])
def getNoticeList():

	noticeQuery = "SELECT * FROM notices \
					WHERE notice_id in (SELECT notice_id FROM flat_addr WHERE flat_id=%d)" % (session['flatId'])
	CURSOR.execute(noticeQuery)

	result = CURSOR.fetchall()
	noticeList = [{'subject':row[2], 'date':str(row[3]), 'body':row[4]} for row in result]
	
	noticeList = json.dumps(noticeList)
	return noticeList


@app.route('/dashboard', methods=['GET'])
def userDashboard():
	return render_template('user/userdashboard.html')

@app.route('/bills')
def userBill():
	#billQuery = 'SELECT * FROM '
	billListQuery = "SELECT due_date, amount, bill_num \
					FROM maintenance_bill \
					WHERE flat_id='%d'\
					ORDER BY due_date DESC" % (session['flatId'])

	CURSOR.execute(billListQuery)
	latest_bill = CURSOR.fetchone()
	billList = [{'date': date, 'amount': amount} for (date, amount) in CURSOR.fetchall()]
	
	categories = ['WATER CHARGES', 'PROPERTY TAX', 'ELECTRICITY CHARGES', 'SINKING FUNDS', 'PARKING CHARGES', 'NOC', 'INSURANCE', 'OTHER']

	if len(request.args) <= 0:
		currBillQuery = "SELECT * FROM maintenance_bill WHERE bill_num=%d" % (latest_bill[2])
	else:
		day   = request.args.get('dd')
		month = request.args.get('mm')
		year  = request.args.get('yyyy')
		currBillQuery = "SELECT * FROM maintenance_bill WHERE due_date='%s'" % ('-'.join((year, month, day)))

	CURSOR.execute(currBillQuery)
	currBillResult = CURSOR.fetchone()
	currBill = {}
	currBill['date'] = currBillResult[11]
	currBill['entries'] = [{'category':'WATER CHARGES', 'cost':300},{'category':'PROPERTY TAX', 'cost':1000},{'category':'ELEC CHARGES', 'cost': 400}]
	currBill['amount'] = 2700

	#billList = [{'date': currBill['date'], 'amount': currBill['amount']},{'date': "6/2016", 'amount':2500}, {'date':"5/2016", 'amount':2550}]
	return render_template('user/userbillpage.html', currBill=currBill, billList=billList)

@app.route('/profile')
def userProfile():
		ownerNameQuery = "SELECT owner_name, pending_dues FROM account WHERE acc_name='%s'" % (session['accName'])
		CURSOR.execute(ownerNameQuery)
		ownerRes = CURSOR.fetchone()
		ownerName = ownerRes[0]
		pendingDues = ownerRes[1]

		residentQuery = "SELECT resident_name, resident_id FROM resident WHERE flat_id=%d" % (session['flatId'])
		CURSOR.execute(residentQuery)

		resList = [{'name' :row[0], 'phone': str(1234), 'id': str(row[1])} for row in CURSOR.fetchall()]

		return render_template('user/userprofile.html', ownerName = ownerName, resList = resList, pendingDues = pendingDues)

@app.route('/editDetails', methods=['POST'])
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
def uploadProfileImage():
	if 'profImage' in request.files:
		profImage = request.files['profImage']
		if profImage and allowed_file(profImage):
			profFileName = secure_filename(profImage.filename)
			print(os.path.join(app.config['UPLOAD_FOLDER'], session['societyName'], 'images', profFileName))
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], session['societyName'], 'images', profFileName))

	else:
		flash('Invalid Profile Image upload')

	return redirect(url_for('userProfile'))