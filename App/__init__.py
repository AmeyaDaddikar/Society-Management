from flask import Flask
import os
UPLOAD_FOLDER = os.getcwd() + '/documents'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.secret_key = 'RAO1'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from . import routes
