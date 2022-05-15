from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required,current_user
#getting our random quotes from the quotes API
from ..requests import get_quote
from .forms import BlogForm
from ..models import User,Blog,Comment
# from .. import db,photos

# from flask_login import login_required,current_user

@main.route('/')
def index():
    quote= get_quote()

    return render_template('index.html', quote=quote)



@main.route('/newblog', methods=['GET', 'POST'])
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog_title = form.title.data
        blog_content = form.content.data
        new_blog= Blog(title=blog_title, content=blog_content,user_id=current_user.id)
        new_blog.save_blog()
        flash('Blog created successfully','Success')
        return redirect(url_for('main.index'))
    return render_template('blog.html',blog_form = form)

@main.route('/blog/<blog_id>', methods=['GET', 'POST'])
def blog(blog_id):
    blog=Blog.query.filter_by(id=blog_id).first()
    print(blog)
    return render_template('single.html',blog=blog)