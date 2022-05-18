from . import main
from flask import redirect, render_template, url_for, request
from .forms import BookForm
from app.models import Bookings


@main.route('/')
def index():
  title = 'Welcome to Tours and Travel | Explore your world'

  return render_template('index.html')


@main.route('/bookings', methods=['GET','POST'])
def bookings():
    bookform = BookForm()
    if bookform.validate_on_submit():
      name = bookform.data
      email = bookform.data
      phone = bookform.data
      date = bookform.data
      destination = bookform.data

      new_booking = Bookings(name=na)

      bookform.save_slot()
    return render_template('bookform.html',bookform=bookform)

