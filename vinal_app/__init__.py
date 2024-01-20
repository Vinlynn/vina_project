from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'zKSjsdtSD'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'vinal1_project'

mysql = MySQL(app)

from vinal_app import routes