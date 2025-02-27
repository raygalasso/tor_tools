import os

from flask import Flask, request
import pandas as pd

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='key',
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/onions')
    def onions():
        links = pd.read_json('onions.json')
        return links.to_html()

    @app.route('/hello')
    def hello():
        txt = '<html><body><h1>' + request.remote_addr + '</h1><table>'
        for h in request.headers:

            txt += '<tr><td>' + h[0] + '</td><td>' + h[1] + '</td></tr>'

        txt += '</table></body></html>'
        return txt


    @app.route('/scott.png')
    def scott_jpg():
        txt = '\n' + request.remote_addr + '\n'
        for h in request.headers:

            txt +=  h[0] + ' : ' + h[1] + '\n'

        txt += '\n\n'
        # print txt
        with open("/home/blksun813/scott.txt", "a+") as f:
            f.write(str(datetime.now()))
            f.write(txt)
        return send_file('/home/blksun813/scott.png', mimetype='image/png')


    @app.route('/echo', methods=['GET', 'POST'])
    def echo():
        return range(0, 1024).join(',')

    # register the database commands
    # from flaskr import db
    # db.init_app(app)

    # apply the blueprints to the app
    # from flaskr import auth, blog
    # app.register_blueprint(auth.bp)
    # app.register_blueprint(blog.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule('/', endpoint='index')

    return app

