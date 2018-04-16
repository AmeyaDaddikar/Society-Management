import json
from . import app
from App  import dbconnect
from flask import render_template, request, redirect, url_for, make_response, session, jsonify
import datetime

# PLEASE USE TABS FOR INDENTS RAO

try:
	CONN, CURSOR = dbconnect.connection()
except Exception as e:
	print(e)
	exit()

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	try:
		loginError = request.args.get("loginError")
	except:
		print("No Login Error")
		loginError = None
	
	print(loginError)
	return render_template('index.html',loginError=loginError)

@app.route('/loginCheck', methods=['POST'])
def login():

	accId  = int(request.form['accName'])
	password = request.form['pwd']
	
	if password is None or len(password) == 0:
		password = ''

	accQuery = "SELECT * FROM account \
				WHERE acc_id = %d && acc_pass = '%s'" % (accId, password)

	CURSOR.execute(accQuery)

	if CURSOR.rowcount <= 0:
		return redirect(url_for('index', loginError=True))


	currUser = CURSOR.fetchone()
	session['username'] = currUser[3]
	session['userId']   = currUser[0]
	session['flatId']   = currUser[1]

	societyNameQuery = "SELECT society_name FROM society WHERE society_id in (SELECT society_id FROM flat_addr WHERE flat_id=%d)" % (session['flatId'])
	CURSOR.execute(societyNameQuery)

	session['societyName'] = CURSOR.fetchone()[0]

	return redirect(url_for('userDashboard'))

@app.route('/logout', methods=['GET'])
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@app.route('/refreshNotices', methods=['GET'])
def getNoticeList():

	noticeQuery = "SELECT * FROM notices WHERE notice_id in (SELECT notice_id FROM flat_addr WHERE flat_id=%d)" % (session['flatId'])
	CURSOR.execute(noticeQuery)

	result = CURSOR.fetchall()
	print(result)
	noticeList = [{'subject':row[2], 'date':str(row[3]), 'body':row[4]} for row in result]
	
	noticeList = json.dumps(noticeList)
	return noticeList


@app.route('/dashboard', methods=['GET'])
def userDashboard():
	return render_template('user/userdashboard.html')

@app.route('/bills')
def userBill():
	currBill = {}
	currBill['date'] = "7/2016"
	currBill['categories'] = [{'category':'WATER CHARGES', 'cost':300},{'category':'MAINTAINANCE CHARGES', 'cost':1000},{'category':'PROPERTY TAX', 'cost':1000},{'category':'ELEC CHARGES', 'cost': 400}]
	currBill['amount'] = 2700

	billList = [{'date': currBill['date'], 'amount': currBill['amount']},{'date': "6/2016", 'amount':2500}, {'date':"5/2016", 'amount':2550}]
	return render_template('user/userbillpage.html', currBill=currBill, billList=billList)

@app.route('/profile')
def userProfile():
		ownerNameQuery = "SELECT owner_name, pending_dues FROM account WHERE acc_id=%d" % (session['userId'])
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
		accId = session['userId']
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
		issuesQuery = "SELECT issue_date, issue_desc, related FROM issues WHERE acc_id IN (SELECT acc_id FROM account WHERE flat_id=%d) ORDER BY issue_date" % (session['flatId'])
		CURSOR.execute(issuesQuery)

		issuesList = [{'date': str(row[0]), 'desc': row[1], 'related': row[2]} for row in CURSOR.fetchall()]

		return render_template('user/usercomplaints.html', issuesList = issuesList)
