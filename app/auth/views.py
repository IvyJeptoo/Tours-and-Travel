from flask import render_template, request, flash
from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,logout_user,login_required, current_user
from . import auth
from ..models import User
from .forms import  LoginForm, RegistrationForm
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    title= 'TwendeTours | Log In'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect(url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', title=title, login_form = form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    title = 'TwendeTours | Create account'
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username = form.username.data, email = form.email.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title=title, registration_form=form)
        
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
