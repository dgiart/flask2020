from app import app
from flask import render_template
@app.route('/')


# def foo():
#     return 0
def index():
    l=[1,2,3,4,5,6,7,8,9]
    name1 = 'Artem'
    name2 = 'Html'
    return render_template('index.html', n = name1, m = name2, list=l)
