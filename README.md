# ⚠️ Only for educational purposes! ⚠️
### Phishing panel for Instagram created with Flask
#### Quick start with Debian 10
Clone the repository.
```
https://github.com/nohackingnolife/flask-instagram-phising
```
Create virtual environment and activate it.
```
python3 -m venv venv && . venv/bin/activate
```
Install dependencies.
```
pip install -r requirements.txt
```
Run create_db.py to create a database file. It will create a default user admin, as well.
```
python3 create_db.py
```
Now, you can run the app with gunicorn.
```
gunicorn --bind 127.0.0.1:5000 wsgi:app
```
Admin panel: 127.0.0.1:5000/admin/login (login with admin:admin), in the admin panel you can change the password for admin.

On submitting the form the app redirects a user to Instagram.

If you specify any subpath in the URL, a user will redirected to Instagram with it, for example:
```
http://127.0.0.1:5000/erling.haaland -> https://instagram.com/erling.haaland
```
