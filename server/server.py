from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import os

from exceptions import *

#########################################################
''' @README @TODO @CHANGE

    To set up the server to run on your machine use find (ctrl+f)
    and search for "@CHANGE". This will highlight parts of the code
    that must be edited for the server to properly function

    To start the server simply run this python file:
    $ python server.py
'''
#########################################################

''' ### FLASK SERVER SETUP ### '''

# This code gets the absolute directory for the /../frontend/ folder
root_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
root_dir = os.path.join(root_dir, 'frontend')
# /frontend/static/
static_dir = os.path.join(root_dir, 'static')

#template_folder=template_dir, static_folder=static_dir

# Flask app https://flask.palletsprojects.com/en/2.0.x/
app = Flask(__name__.split('.')[0], root_path=root_dir, template_folder=root_dir, static_folder=static_dir)

''' @CHANGE
    
    ### SQL DATABASE SETUP ###

    Update user, password, and database
'''
try:
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'passwd'
    app.config['MYSQL_DATABASE_PORT'] = 3306    # by default, port is 3306
    app.config['MYSQL_DATABASE_DB'] = 'Group18'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'

    mysql = MySQL()
    mysql.init_app(app)

    db_connection = mysql.connect()
    cursor = db_connection.cursor()
except:
    raise DatabaseError

#########################################################

''' ### REQUESTS HANDLING ### '''

# For help with requests, see: https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/imprint", methods=['GET'])
def imprint():
    return render_template('imprint.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        request_data = request.get_json()

        if request_data:
            print(request_data)
            # cursor.execute("INSERT INTO Visitors (VisitorID, VisitorName, VisitorAddress, VisitorPhoneNumber, VisitorEmail, VisitorDeviceID, VisitorUsername, VisitorPassword) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", ('1', '))
            pass






#########################################################
''' @CHANGE

    This code allows the server to be started by simply
    running this python file with the following command
    in this directory:

    $ python server.py
'''

if __name__ == '__main__': 
    app.run(debug=True, port=5000)
#########################################################




