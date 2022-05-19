from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User




class RegistrationForm(FlaskForm):
    username = StringField('Enter Username:', validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Enter email address:', validators=[DataRequired(),Email()])
    password = PasswordField('Password:', validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password:', validators=[DataRequired()])
    submit = SubmitField('SignUp')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Enter your email:', validators=[DataRequired(), Email()])
    password = PasswordField('Enter your password:', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log In')