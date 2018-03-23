from . import app
from flask import render_template, request

# OPTIONAL/ REQUIRED ARGUMENT LIST
# 1. title (base.html) : Displays the title of the page


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html')
