from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField(
        'Password', validators=[validators.DataRequired(), validators.Length(min=4)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Submit')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('New password', validators=[validators.DataRequired(
    ), validators.EqualTo('confirm', message='Passwords must match'), validators.Length(min=4)])
    confirm = PasswordField('Repeat password')
    submit = SubmitField('Submit')
