import datetime
from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, DateField, FloatField, DecimalField, IntegerField, FieldList, FormField, HiddenField, SelectMultipleField
from wtforms.widgets import TextArea, CheckboxInput, ListWidget
from wtforms import validators
from wtforms.validators import DataRequired, Optional
from flask import flash, session
from App  import dbconnect
from random import randint

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
						INNER JOIN flat ON account.flat_id=flat.flat_id \
						INNER JOIN wing ON flat.wing_id=wing.wing_id \
						INNER JOIN society ON wing.society_id=society.society_id \
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
	billDate      = DateField('Bill Date', format='%Y-%m-%d', validators=[DataRequired()])
	dueDate       = DateField('Due Date',  format='%Y-%m-%d', validators=[DataRequired()])
	selectedWings = SelectMultipleField('Wings', choices=[],widget=ListWidget(prefix_label=False),option_widget=CheckboxInput(), validators=[DataRequired()])
	WATER_CHARGES		=DecimalField(label='WATER CHARGES'       ,places=2, validators=[DataRequired()])
	PROPERTY_TAX		=DecimalField(label='PROPERTY TAX'        ,places=2, validators=[DataRequired()])
	ELECTRICITY_CHARGES=DecimalField(label='ELECTRICITY CHARGES',places=2, validators=[DataRequired()])
	SINKING_FUNDS		=DecimalField(label='SINKING FUNDS'       ,places=2, validators=[DataRequired()])
	PARKING_CHARGES		=DecimalField(label='PARKING CHARGES'     ,places=2, validators=[DataRequired()])
	NOC					=DecimalField(label='NOC'       ,places=2, validators=[DataRequired()])
	INSURANCE			=DecimalField(label='INSURANCE' ,places=2, validators=[DataRequired()])
	OTHER				=DecimalField(label='OTHER'     ,places=2, validators=[Optional()])
	submitBtn = SubmitField(label='Submit')

class AddSocietyForm(FlaskForm):
	societyName = StringField (label='Society Name', validators=[DataRequired()])
	adminName   = StringField (label='Admin Account Name', validators=[DataRequired()])
	adminPass   = PasswordField (label='Admin Password', validators=[DataRequired()])
	region      = StringField (label='Address', widget=TextArea(), validators=[DataRequired(), validators.Length(min=5, max=127, message='Invalid Address Length')])
	city        = StringField (label='City', validators=[DataRequired()])
	state       = StringField (label='State', validators=[DataRequired()])
	area        = IntegerField(label='Area of land', validators=[DataRequired()])
	totalWings  = IntegerField(label='Total Wings in the Society', validators=[DataRequired()])
	submitBtn   = SubmitField(label='Submit')
	
	def validate(self):
		validInput=FlaskForm.validate(self)
		if not validInput:
			return False
		CURSOR.execute("INSERT INTO society(society_name, region, city, state, area) VALUES (%s, %s, %s, %s, %s)", [self.societyName.data, self.region.data, self.city.data, self.state.data, int(self.area.data)])
		CURSOR.execute("SELECT society_id FROM society WHERE society_name=%s", [self.societyName.data])
		socRes=CURSOR.fetchone()
		socId=socRes[0]
		CURSOR.execute("INSERT INTO admin(acc_name, society_id, admin_pass) VALUES(%s, %s, %s)", [self.adminName.data, int(socId), self.adminPass.data])
		CONN.commit()
		return True

class AddWingForm(FlaskForm):
	wingName    = StringField (label='Wing Name', validators=[DataRequired()])
	totalFloors = IntegerField(label='Total Floors', validators=[DataRequired()])
	totalArea   = IntegerField(label='Total Area', validators=[DataRequired()])
	totalFlats  = IntegerField(label='Flats', validators=[DataRequired()])

class WingForms(FlaskForm):
	wings     = FieldList(FormField(AddWingForm, 'Wing'), min_entries=1)
	submitBtn = SubmitField(label='Submit')

class AddFlatForm(FlaskForm):
	flatNum    = IntegerField(label='Flat Number', validators=[DataRequired()])
	flatFacing = StringField (label='Flat Facing', validators=[DataRequired()])
	area       = IntegerField(label='Area', validators=[DataRequired()])
	BHK        = DecimalField(label='Total BHK' ,places=1, validators=[DataRequired()])
	floorNum   = IntegerField(label='Area', validators=[DataRequired()])
	price      = DecimalField(label='OTHER' ,places=2, validators=[DataRequired()])

class WingFlats(FlaskForm):
	wingId    = HiddenField("wingId")
	flats     = FieldList(FormField(AddFlatForm, 'flat'), min_entries=1)
	submitBtn = SubmitField(label='Submit')

class AddResident(FlaskForm):
	name    = StringField (label='Name', validators=[DataRequired()])
	contact = IntegerField(label='Contact', validators=[DataRequired()])
	submitBtn = SubmitField(label='Submit')