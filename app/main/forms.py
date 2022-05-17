from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, SelectField, DateField
from wtforms.validators import InputRequired


class BookForm(FlaskForm):
    Name = StringField('Enter your name')
    Email = StringField('Enter email address')
    Phone = StringField('Enter phone number')
    Location = StringField('Enter')
    Date = DateField('Selected date')
    Destination = SelectField('Select your destination')
    Book = SubmitField('Book')
    
