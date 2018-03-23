
## Configurations

1. To run the flask server
'''
export FLASK_APP=start.py

flask run --host=0.0.0.0:5000

#if the above line doesn't work, use :
python3 -m flask run --host=0.0.0.0:5000

#host is optional, and should not matter unless you want to test the application on a physical device on your network.
'''

2. To use the virtual environment
'''
./venv/bin/activate
#OR
source venv/bin/activite
'''
