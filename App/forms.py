import datetime
from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, DateField, FloatField, DecimalField
from wtforms.widgets import TextArea
from wtforms import validators
from wtforms.validators import DataRequired, Optional
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
			accQuery = 'SELECT acc_name, society_id, resident_id \
			FROM admin \
			WHERE acc_name="%s" && admin_pass = "%s"' % (accName, password)

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

class AddNoticeForm(FlaskForm):
	header  = StringField(label='Title/Subject', validators=[validators.Length(min=3, max=63, message='Invalid header')])
	date    = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
	body    = StringField('Descripion', widget=TextArea(), validators=[DataRequired()])
	submitBtn = SubmitField(label='Submit')

	def validate(self):
		validInput = FlaskForm.validate(self)
		if not validInput:
			return False
		# flash('Add this to DB Rao')
		CURSOR.execute("INSERT INTO notices(society_id, notice_header, notice_date, notice_desc) VALUES (%s, %s, %s, %s)", [int(session['societyId']), self.header.data, self.date.data, self.body.data])
		CONN.commit()
		print("Hello World!")
		return True

#Categories and their corresponding indices upon * request of maintenance_bill
#categories = {'WATER CHARGES':3, 'PROPERTY TAX':4, 'ELECTRICITY CHARGES':5, 'SINKING FUNDS':6, 'PARKING CHARGES':7, 'NOC':8, 'INSURANCE':9, 'OTHER':10}

class AddBillForm(FlaskForm):
	billDate    = DateField('Bill Date', format='%Y-%m-%d', validators=[DataRequired()])
	dueDate     = DateField('Due Date',  format='%Y-%m-%d', validators=[DataRequired()])

	WATER_CHARGES		=DecimalField(label='WATER CHARGES'       ,places=2, validators=[DataRequired()])
	PROPERTY_TAX		=DecimalField(label='PROPERTY TAX'        ,places=2, validators=[DataRequired()])
	ELECTRICITY_CHARGES=DecimalField(label='ELECTRICITY CHARGES',places=2, validators=[DataRequired()])
	SINKING_FUNDS		=DecimalField(label='SINKING FUNDS'       ,places=2, validators=[DataRequired()])
	PARKING_CHARGES		=DecimalField(label='PARKING CHARGES'     ,places=2, validators=[DataRequired()])
	NOC					=DecimalField(label='NOC'       ,places=2, validators=[DataRequired()])
	INSURANCE			=DecimalField(label='INSURANCE' ,places=2, validators=[DataRequired()])
	OTHER				=DecimalField(label='OTHER'     ,places=2, validators=[Optional()])
	submitBtn = SubmitField(label='Submit')
