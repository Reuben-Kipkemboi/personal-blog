from datetime import datetime
from sqlalchemy import false
from . import db
#securing passwords
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


#have a class quotes for our random quotes    
class Quotes():
    '''
    Defining Quote objects
    '''
    def __init__(self, quote, author, permalink):
        self.quote = quote
        self.author  = author
        self.permalink = permalink
        
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Class User
class User(UserMixin, db.Model):  
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_secure = db.Column(db.String(255))
    description = db.Column(db.String(255))
    avatar = db.Column(db.String())
    blogs = db.relationship('Blog', backref='author', lazy = 'dynamic')
     # save user
    def save_user(self):
        db.session.add(self)
        db.session.commit()
        
    # hashing password by some cryptographic means
    @property
    def password(self):
        raise AttributeError('You cant access password attribute')
    
    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)
        
    # check password
    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)
    
    # login manager
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'User {self.username}'

    #Initializing user properties
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
       
#Blogs class
class Blog(db.Model):  
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(255))
    blog_content = db.Column(db.String())
    date_posted=db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='blog', lazy = 'dynamic')
    
    #saving our blogs
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    def repr(self):
        return f'Blog {self.blog_title}'
#Comments class

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.String(255))
    date_commented=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Comment {self.name}'