from phishing import db, app
from phishing.models import User
from werkzeug.security import generate_password_hash
app.app_context().push()
db.create_all()
user = User(username='admin', password=generate_password_hash('admin'))
db.session.add(user)
db.session.commit()
