from flask import Blueprint
from flask import render_template


posts = Blueprint('posts', __name__, template_folder = 'templates')

@posts.route('/')
def index():
    name1 = 'Artem'
    name2 = 'HtmlBlueprint'
    return render_template('posts/index.html', n = name1, m = name2)
