import json
from . import app
from flask import render_template, request, redirect, url_for, make_response, session, jsonify

# OPTIONAL/ REQUIRED ARGUMENT LIST
# 1. title (base.html) : Displays the title of the page


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
	accName  = request.form['accName']
	password = request.form['pwd']
	

	#DATABASE CHECKS
	if accName not in ['Ameya', 'Vineet']:
		return redirect(url_for('index', loginError=True))
		
	session['username'] = accName

	return redirect(url_for('userDashboard'))

@app.route('/logout', methods=['GET'])
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))

@app.route('/refreshNotices', methods=['GET'])
def getNoticeList():

	noticeList = [{'subject': "Notice 1", 'date': "28/07/1998", 'body': "This is notice 1"},{'subject': "Notice 2", 'date': "10/08/1998", 'body': "This is notice 2"}]

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
