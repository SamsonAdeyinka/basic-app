from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from application import routes
