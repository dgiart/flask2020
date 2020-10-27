from app import app
from flask import render_template
@app.route('/')
def index():
    name1 = 'Art'
    name2 = 'Html'
    return render_template('index.html', n = name1, m = name2)
