from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Email


class BookForm(FlaskForm):
    name = StringField('Enter your name:', validators=[DataRequired()])
    email = StringField('Enter email address:', validators=[DataRequired(), Email()])
    phone = StringField('Enter phone number:', validators=[DataRequired()])
    location = StringField('Enter your location:', validators=[DataRequired()])
    date = DateField('Selected date:', validators=[DataRequired()])
    destination = SelectField('Select your destination:',choices=[('South Coast'),('North Coast'),('Lake Region'),('Mt. Kenya Region'),('Rift Valley region'),('Nakuru')], validators=[DataRequired()])
    book = SubmitField('Book')

    
    
