from . import main
from flask import redirect, render_template, url_for, request,flash
from flask_login import current_user, login_required
from ..models import Comment
from app import db
from .forms import BookForm
from app.models import Bookings


@main.route('/')
def index():
  title = 'Welcome to Tours and Travel | Explore your world'
  return render_template('index.html',title=title)


@main.route('/profile')
@login_required
def profile():
  title = 'Welcome to Tours and Travel | Your profile'
  user_id = current_user._get_current_object().id
  bookings = Bookings.query.filter_by(user_id=user_id).all()
  return render_template('profile/profile.html', title=title, bookings=bookings)



@main.route('/comments')
def comments():
  allcomments = Comment.query.all()
  print(allcomments)
  
  return render_template('comments.html', allcomments=allcomments)


@main.route('/comment',methods=['GET','POST'])
@login_required
def comment():
    if request.method == 'POST':        
        message = request.form.get('message')
        nickname = request.form.get('nickname')        
        new_comment = Comment(message=message,nickname=nickname)
        
        db.session.add(new_comment)
        db.session.commit()
        print(new_comment)
        
        return redirect(url_for('main.comments')) 
    
    return render_template('comments.html')
  
@main.route('/remove/<int:comment_id>', methods=['GET','POST'])
@login_required
def deletecomment(comment_id):
        comment = Comment.query.get_or_404(comment_id)
    
        db.session.delete(comment)
        db.session.commit()        
        flash("comment deleted!",category='success')
        return render_template ('comments.html')
  


@main.route('/bookings', methods=['GET','POST'])
def bookings():
    bookform = BookForm()
    if bookform.validate_on_submit():
      name = bookform.name.data
      email = bookform.email.data
      phone_number = bookform.phone.data
      date = bookform.date.data
      location = bookform.location.data
      destination = bookform.destination.data
      user_id = current_user._get_current_object().id

      bookings = Bookings(name=name, email=email, phone_number=phone_number, date=date, location=location, destination=destination, user_id=user_id)
      bookings.save_bookings()
      return redirect(url_for('main.profile'))


    return render_template('bookform.html',bookform=bookform)

