from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired
from flask import flash, session
from App  import dbconnect

try:
	CONN, CURSOR = dbconnect.connection()
except Exception as e:
	print(e)
	exit()

class LoginForm(FlaskForm):
	accName   = StringField(label='Account Name', validators=[validators.Length(min=4, max=25, message='Invalid Account Name')])
	password  = PasswordField(label='Password', validators=[validators.Length(min=4, max=25, message='Invalid Password')])
	accType   = RadioField(label='Account Type', choices=[('FlatAcc','Flat Account'),('AdminAcc','Admin Account')], validators=[DataRequired()])
	submitBtn = SubmitField(label='Submit')

	def validate(self):
		validInput = FlaskForm.validate(self)
		if not validInput:
			return False

		accName  = self.accName.data
		password = self.password.data

		if self.accType.data == 'FlatAcc':
			accQuery = "SELECT account.acc_name, account.owner_name, account.flat_id, society.society_name, society.society_id FROM account \
						LEFT JOIN flat_addr ON account.flat_id=flat_addr.flat_id \
						LEFT JOIN society ON flat_addr.society_id=society.society_id \
						WHERE acc_name = '%s' && acc_pass = '%s'" % (accName, password)

		# ADMIN TABLE HAS A PASSWORD FIELD, BUT WE ARE CHECKING PASSWORD FROM ACCOUNT TABLE
		elif self.accType.data == 'AdminAcc':
			accQuery = 'SELECT account_name, society_id, resident_id \
			FROM admin_view INNER JOIN account \
			ON admin_view.account_name=account.acc_name \
			WHERE acc_name="%s" && acc_pass = "%s"' % (accName, password)

		CURSOR.execute(accQuery)
		if CURSOR.rowcount <= 0:
			flash('INVALID LOGIN DETAILS')
			return False

		currUser = CURSOR.fetchone()

		if self.accType.data == 'FlatAcc':
			session['mainPage'] = '/dashboard'
			session['accName']     = currUser[0]
			session['ownerName']   = currUser[1]
			session['flatId']      = currUser[2]
			session['societyName'] = currUser[3]
			session['societyId']   = currUser[4]
		else:
			session['mainPage'] = '/admin'
			session['accName']     = currUser[0]
			session['societyId']   = currUser[1]

			societyAdminQuery = "SELECT society_name FROM society WHERE society_id=%d" % (session['societyId'])
			CURSOR.execute(societyAdminQuery)
			session['societyName'] = CURSOR.fetchone()[0]
			session['ownerName']   = currUser[0]

		return True