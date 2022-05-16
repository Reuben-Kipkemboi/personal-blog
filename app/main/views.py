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
    blogs = Blog.query.order_by(Blog.date_created.desc()).all()
    quote= get_quote()

    return render_template('index.html', quote=quote, blogs=blogs   )

@main.route('/newblog', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog_title = form.title.data
        blog_content = form.content.data
        new_user_blog= Blog(blog_title=blog_title, blog_content=blog_content,user_id=current_user.id)
        
        
        new_user_blog.save_blog()
        
        flash('Blog created successfully','Success')
        
        return redirect(url_for('main.index'))
    
    return render_template('blog.html',form = form)

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
@login_required
def delete_user_comment(comment_id):
    comment = Comment.query.filter_by(id = comment_id).first()
    blog_id = comment.blog_id
    db.session.delete(comment)
    db.session.commit()
    flash('successfully Deleted comment','success')
    return redirect(url_for('blog.html',blog_id = blog_id))

#Updating a blog
@main.route('/blog/<blog_id>/updating',methods=['GET', 'POST'])
@login_required
def update_blog(blog_id):
    user_blog=Blog.query.filter_by(id=blog_id).first()
    #Checks the user by using the id
    if user_blog.author.id !=current_user.id:
        abort(403)

    form=BlogForm()
    if form.validate_on_submit():
        user_blog.blog_title=form.title.data
        user_blog.blog_content=form.content.data
        db.session.commit()
        flash('You have updated a blog','Success')
        return redirect(url_for('.blog',blog_id=blog.id) )
    elif request.method=='GET':
        form.title.data=user_blog.blog_title
        form.content.data=user_blog.blog_content    
    return render_template('blog.html', form = form,title='Update blog update')


#Deleting a blog
@main.route('/blog/<blog_id>/deleting',methods=['GET', 'POST'])
@login_required
def delete_user_blog(blog_id):
    user_blog=Blog.query.filter_by(id=blog_id).first()
    
    db.session.delete(user_blog)
    db.session.commit()
    return redirect(url_for('main.index'))