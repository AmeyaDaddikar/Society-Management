from flask import Flask
import os
STATIC_FOLDER = os.getcwd()   + '/App/static'
UPLOAD_FOLDER = STATIC_FOLDER + '/documents'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read_file(filename):
	with open(filename, 'rb') as f:
		photo = f.read()
	return photo

app = Flask(__name__)
app.secret_key = 'RAO1'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from . import routes
