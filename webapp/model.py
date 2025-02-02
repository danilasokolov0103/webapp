from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class News(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        published = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return '<News {} {}>'.format(self.title, self.url)

class User(db.Model,UserMixin):
    id =  db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), index = True, unique = True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index = True)


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)


    @property
    def is_admin(self):
        return self.role == 'admin' 

    
    def check_password(self, password):
        return check_password_hash(self.password, password)