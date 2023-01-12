from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = "jFSDFJj213^DF&*123jefhsF_Dh09gd0-=adm"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phishing.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from .models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


from . import routes
