from flask import Flask

app = Flask(__name__)
app.secret_key = 'RAO1'

from . import routes
