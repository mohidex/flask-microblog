from flask import render_template
from app.post import bp
from flask_login import login_required
from app.models import Post


@login_required
@bp.route('/post/<int:post_id>')
def post_detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post/detail_post.html', title=post.title, post=post)
