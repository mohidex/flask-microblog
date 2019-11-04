from flask import render_template, flash, redirect, url_for, abort
from app.post import bp
from app import db
from flask_login import login_required, current_user
from app.models import Post
from app.post.forms import PostForm


@login_required
@bp.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post/detail_post.html', title=post.title, post=post)


@login_required
@bp.route('/post/new-post', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post is now live!')
        return redirect(url_for('main.index'))
    return render_template('post/create_post.html', title='New Post', form=form)


@bp.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        flash('Your post has been updated!')
        return redirect(url_for('post.post_detail', post_id=post.id))
    form.title.data = post.title
    form.body.data = post.body
    return render_template('post/create_post.html', title='Update Post', form=form)



@bp.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('You post has been deleted!')
    return redirect(url_for('main.index'))
