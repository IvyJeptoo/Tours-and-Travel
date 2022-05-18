from .import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import db




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