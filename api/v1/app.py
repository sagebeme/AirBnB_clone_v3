#!/usr/bin/python3
"""
    Flask App
"""
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def name():
    """
    teardown:calls storage close
    """
    storage.close
# end def


@app.route('/')
def name():
    """
    Purpose:
    """

# end def


if __name__ == "__main__":
    """
    Main function
    """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = 5000
    app.run(host=host, port=port, threaded=True)