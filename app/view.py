from app import app
import logging
logger = logging.getLogger()
from flask import render_template
@app.route('/')
def index():

    logger.warning('!!!!!!!!!!!!!')
    print(22222222222222222)
    l=[1,2,3,4,5,6,7,8,9]
    name1 = 'Artem'
    name2 = 'Html'
    return render_template('index.html', n = name1, m = name2, list=l)
