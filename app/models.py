from . import db 

from sqlalchemy.sql import func

from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class Comment(db.Model):
    '''
    create comment schema for the comment table
    '''
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))

class Bookings(db.Model):


    __tablename__ = 'bookings'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, index=True, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())
    destination = db.Column(db.String, nullable=False)

    
    def __repr__(self):
        return f'User {self.name}'
