import json
from . import app
from App  import dbconnect
from flask import render_template, request, redirect, url_for, make_response, session, jsonify

# OPTIONAL/ REQUIRED ARGUMENT LIST
# 1. title (base.html) : Displays the title of the page

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
	#noticeList = [{'subject': "Notice 1", 'date': "28/07/1998", 'body': "This is notice 1"},{'subject': "Notice 2", 'date': "10/08/1998", 'body': "This is notice 2"}]

	noticeList = json.dumps(noticeList)
	return noticeList


@app.route('/dashboard', methods=['GET'])
def userDashboard():
	return render_template('user/userdashboard.html', user= request.args.get("accName"))

@app.route('/bills')
def userBill():
	return render_template('user/userbillpage.html')

@app.route('/profile')
def userProfile():
	return render_template('user/userprofile.html')

@app.route('/editDetails', methods=['POST'])
def updateUserDetails():
	#DO ALL DATABASE UPDATES HERE
	return render_template('user/userprofile.html')

@app.route('/issues', methods=['GET', 'POST'])
def getComplaints():
	#get the POST DATA from forms if submitted
	return render_template('user/usercomplaints.html')
