from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired
from App  import dbconnect

try:
	CONN, CURSOR = dbconnect.connection()
except Exception as e:
	print(e)
	exit()

class LoginForm(FlaskForm):
	accName   = StringField(label='Account Name', validators=[validators.Length(min=4, max=25, message='Invalid Account Name')])
	password  = PasswordField(label='Password', validators=[validators.Length(min=4, max=25, message='Invalid Password')])
	accType   = RadioField(label='Account Type', choices=[('FlatAcc','Flat Account'),('AdminAcc','Admin Account')])
	submitBtn = SubmitField(label='Submit')

	def validate(self):
		validInput = FlaskForm.validate(self)
		if not validInput:
			return False

		accName  = self.accName.data
		password = self.password.data
		
		return True