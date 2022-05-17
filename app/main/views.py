from . import main
from flask import redirect, render_template, url_for, request
from .forms import BookForm



@main.route('/')
def index():
  title = 'Welcome to Tours and Travel | Explore your world'

  return render_template('index.html')


@main.route('/', methods=['GET','POST'])
def book_slot():
    book_form = BookForm()
    if book_form.validate_on_submit():
      name = book_form.data
      email = book_form.data
      phone = book_form.data
      date = book_form.data
      destination = book_form.data

      book_form.save_slot()
      return render_template('bookform.html',book_form=book_form)

