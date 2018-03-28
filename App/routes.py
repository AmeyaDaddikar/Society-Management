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
		
	return redirect(url_for('userDashboard'))

@app.route('/dashboard', methods=['GET'])

def userDashboard():
	return render_template('userdashboard.html')

