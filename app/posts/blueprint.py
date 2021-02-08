from flask import Blueprint
from flask import render_template
from flask import request
from models import Post, Tag
from app import db

from . forms import PostForm

posts = Blueprint('posts', __name__, template_folder = 'templates')



@posts.route('/create')
def create_post():
    form=PostForm()
    return render_template('posts/post_create.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('Q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
        # if posts.count() == 0:
        #     not_found='No results found'
        #     p=Post(title=not_found)
        #
        #     posts = Post.query.filter(Post.title.contains(not_found))
    else:
        posts = Post.query.all()
    return render_template('posts/index.html', posts = posts)

@posts.route('/<slug>')
def post_detail(slug):
    post=Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post = post, tags = tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/tag_detail.html', tag = tag, posts = posts)
