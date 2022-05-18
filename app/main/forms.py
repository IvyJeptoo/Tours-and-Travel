from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Email


class BookForm(FlaskForm):
    name = StringField('Enter your name')
    email = StringField('Enter email address')
    phone = StringField('Enter phone number')
    location = StringField('Enter your location')
    date = DateField('Selected date')
    destination = SelectField('Select your destination',choices=[('South Coast'),('North Coast'),('Lake Region'),('Mt. Kenya Region'),('Rift Valley region'),('Nakuru')])
    book = SubmitField('Book')

    
    
