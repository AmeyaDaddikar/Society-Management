from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
UPLOAD_FOLDER = os.getcwd() + '/documents'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.secret_key = 'RAO1'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:c1o2l3d4@localhost/society_mysqldb'

db = SQLAlchemy(app)

from . import models
