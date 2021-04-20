
from app import app
from app import db


from posts.blueprint import posts

app.register_blueprint(posts, url_prefix = '/blog')

import view

if __name__ == '__main__':
    import sys
    print(sys.version)
    app.run()
