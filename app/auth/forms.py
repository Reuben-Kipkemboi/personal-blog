from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError


#Defining our forms
class RegistrationForm(FlaskForm):
    email = StringField('Provide your Email Address',validators=[DataRequired(),Email()])
    username = StringField('Provide your Username',validators = [DataRequired()])
    password = PasswordField('User Password/passcode',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm your password/passcode',validators = [DataRequired()])
    submit = SubmitField('Sign Up to BlogSpot')
    
    #validating our email
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('An account with that email exists')

    #validating our username
    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username is already taken')
        
        
#login form
class LoginForm(FlaskForm):
    email = StringField('Provide Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Provide your password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In to Blogspot')