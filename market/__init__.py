from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY']='2fbed2422e43247fcd8f01b4' # this will be get if you write in terminal python>>> import os>>> os.urandom(12).hex()
db = SQLAlchemy(app)
app.app_context().push()
bcrypt=Bcrypt(app)      # it convert the password into hash value
login_manager=LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category="info"
from market import route
