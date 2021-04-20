from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from models import Post, Tag
from app import db
import logging

from flask_security import login_required

logger = logging.getLogger()



from . forms import PostForm

posts = Blueprint('posts', __name__, template_folder = 'templates')



@posts.route('/create', methods=['POST', 'GET'])
@login_required
def create_post():
    if request.method == 'POST':
        title=request.form['title']
        body=request.form['body']

        try:
            post=Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Smth went Wrong')
        return redirect(url_for('posts.index'))
    form=PostForm()
    return render_template('posts/post_create.html', form = form)


@posts.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug == slug).first()
    if request.method == 'POST':

        form = PostForm(formdata = request.form, obj = post)
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('posts.post_detail', slug = slug) )
    form = PostForm(obj = post)
    return render_template('/posts/post_edit.html', form = form, post = post)


@posts.route('/')
def index():
    q = request.args.get('Q')
    page=request.args.get('page')


    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
        # num_posts = posts.count()
    else:
        posts = Post.query.order_by(Post.created.desc())

    num_posts = posts.count()
    # logger.warning('!!!!!number Of POSTS = ' + str(num_posts))
    # logger.warning('!!!!!PAGE number = ' + str(page))

    if page and page.isdigit():
        page=int(page)
        if page >= num_posts:
            page = 1
    else:
        page = 1



    pages=posts.paginate(page=page, per_page=5)
    return render_template('posts/index.html', posts = posts, pages=pages)

@posts.route('/<slug>')
def post_detail(slug):
    q = request.args.get('Q')
    if q:
        return redirect(url_for('posts.index'))

    post=Post.query.filter(Post.slug==slug).first()
    logger.warning('SLUG =' + slug)
    tags = post.tags
    return render_template('posts/post_detail.html', post = post, tags = tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    q = request.args.get('Q')
    if q:
        return redirect(url_for('posts.index'))
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag = tag, posts = posts)
