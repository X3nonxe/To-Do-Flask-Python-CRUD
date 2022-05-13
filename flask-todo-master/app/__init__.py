from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'thisismysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://xenonxe:X3n0nx3@localhost/database_ku'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'xenonxe'
app.config['MYSQL_PASSWORD'] = 'X3n0nx3'
app.config['MYSQL_DB'] = 'database_ku'

mysql = MySQL(app)

from app import routes
