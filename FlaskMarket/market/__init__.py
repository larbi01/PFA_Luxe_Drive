from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager





app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images'
app.config['UPLOAD_CSS'] = 'templates/static/css'
app.config['UPLOAD_JS'] = 'templates/static/js'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'location_voiture'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/location_voiture'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key_here'


mysql = MySQL(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from market.models import Login
    login = Login(1, 'sdf', 'sdf', 'sdf')
    user = login.get_user_by_id(user_id)
    return user


from market import forms, login_manager
from market import routes

