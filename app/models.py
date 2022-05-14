import datetime
from . import db
   #securing passwords
from werkzeug.security import generate_password_hash,check_password_hash
class User(db.Model):  
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_secure = db.Column(db.String(255))
    description = db.Column(db.String(255))
    avatar = db.Column(db.String())
    blogs = db.relationship('Blogs', backref='author', lazy = 'dynamic')
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
        self.password_hash = generate_password_hash(password)
    # check password
    def verify_password(self, password):
        return check_password_hash(self.password_secure, password)
    # login manager
    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.query.get(int(user_id))
    def __repr__(self):
        return f'User {self.username}'

    #Initializing user properties
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        
#have a class quotes for our random quotes    
class Quotes():
    '''
    Defining Quote objects
    '''
    def __init__(self, quote, author, permalink):
        self.quote = quote
        self.author  = author
        self.permalink = permalink
        