from . import db, login_manager
from sqlalchemy.sql import func
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    gender = db.Column(db.String(128), default='Undisclosed')
    pass_code = db.Column(db.String(60), nullable=False)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    bookings = db.relationship('Bookings', backref='user', lazy='dynamic')



    @property
    def password(self):
        raise AttributeError('You cannot access the password')


    @password.setter
    def password(self, password):
        self.pass_code= generate_password_hash(password)


    def verify_password(self, password):
        return check_password_hash(self.pass_code, password)


    def __repr__(self):
        return f"User( '{self.username}','{self.email}','{self.gender}')"


class Comment(db.Model):
    '''
    create comment schema for the comment table
    '''
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

class Bookings(db.Model):


    __tablename__ = 'bookings'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    destination = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))



    def save_bookings(self):
        db.session.add(self)
        db.session.commit()

    
    def __repr__(self):
        return f'User {self.name}'
