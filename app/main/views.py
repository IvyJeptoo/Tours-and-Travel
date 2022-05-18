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
      name = bookform.name.data
      email = bookform.email.data
      phone = bookform.phone.data
      date = bookform.date.data
      destination = bookform.destination.data

      Bookings = Bookings(name=name, email=email, phone=phone, date=date, destination=destination)

      bookform.save_slot()
    return render_template('bookform.html',bookform=bookform)

