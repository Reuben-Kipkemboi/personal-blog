from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,RadioField,TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo
from ..models import User,Blogs,Comment


class BlogForm(FlaskForm):
    title = StringField('Enter your Blog Title', validators=[DataRequired(), Length(1, 64)])
    author = StringField('Blog Author Name',)
    blog_category = RadioField('Blog Category :', choices = [('Technology', 'Technology'),  ('Lifestyle', ' Lifestyle'), ('Farming', 'Farming'),('Vehicles & Transport' , 'Vehicles and Transport'), ('Fashion and Clothing', 'Fashion & Clothing', ('Education', 'Education'))], validators = [DataRequired()])
    content = TextAreaField('Blog content')
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = TextAreaField('Give Feedback, Complaints/Comments', validators=[DataRequired()])

    submit = SubmitField('COMMENT')