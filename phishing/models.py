from flask_login import UserMixin
from phishing import db


class Log(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=100), nullable=False)
    password = db.Column(db.String(length=100), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f'Log {self.username}'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=100), unique=True)
    password = db.Column(db.String(length=100))
