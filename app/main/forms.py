from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Email


class BookForm(FlaskForm):
    name = StringField('Enter your name')
    email = StringField('Enter email address')
    phone = StringField('Enter phone number')
    location = StringField('Enter')
    date = DateField('Selected date')
    destination = SelectField('Select your destination')
    book = SubmitField('Book')
    
