from . import main
from flask import redirect, render_template, url_for, request,flash
from flask_login import login_required
from ..models import Comment
from app import db


@main.route('/')
def index():
  title = 'Welcome to Tours and Travel | Explore your world'

  return render_template('index.html',title=title)
@main.route('/profile')
def profile():
  
  return render_template('profile.html')

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