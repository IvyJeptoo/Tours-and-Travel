from . import main
from flask import redirect, render_template, url_for, request


@main.route('/')
def index():
  title = 'Welcome to Tours and Travel | Explore your world'

  return render_template('index.html')
@main.route('/profile')
def profile():
  
  return render_template('profile.html')

@main.route('/comments')
def comments():
  
  return render_template('comments.html')