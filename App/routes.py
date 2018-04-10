from . import app
from flask import render_template, request, redirect, url_for, make_response

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
	
	#validate accName and password here
	#replace this condition
	if accName != 'Ameya':
		return redirect(url_for('index', loginError=True))
		
	return redirect(url_for('userDashboard', accName = accName))

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