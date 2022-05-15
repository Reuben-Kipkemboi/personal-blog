from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from..import db
from flask_login import login_required,current_user
#getting our random quotes from the quotes API
from ..requests import get_quote
from .forms import BlogForm,CommentForm
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

#Displaying our blogs
@main.route('/blog/<blog_id>', methods=['GET', 'POST'])
def blog(blog_id):
    blog=Blog.query.filter_by(id=blog_id).first()
    print(blog)
    return render_template('single.html',blog=blog)

#Commenting on anew blog
@main.route('/comment/<blog_id>', methods=['GET', 'POST'])
def make_comment(blog_id):
    user_comments = Comment.query.filter_by(blog_id=blog_id).all()
    blog = Blog.query.get(blog_id)
    form = CommentForm()
    #If blog does not exist
    if blog is None:
        abort(404)
    if form.validate_on_submit():
            comment = Comment(comment_content=form.content.data,blog_id=blog_id,
            user_id=current_user.id)
            db.session.add(comment)
            db.session.commit()
            #Reset form after submitting comment
            form.content.data = ''
            flash('Thank you for your comment, Looking forward for more!','success')
    return render_template('comment.html',blog= blog, user_comments =user_comments, form = form)

#Deleting insulting or degrading comments.
@main.route('/comment/<comment_id>', methods=['POST','GET'])
def delete_user_comment(comment_id):
    comment = Comment.query.filter_by(id = comment_id).first()
    blog_id = comment.blog_id
    db.session.delete(comment)
    db.session.commit()
    flash('successfully Deleted comment','success')
    return redirect(url_for('.blog',blog_id = blog_id))