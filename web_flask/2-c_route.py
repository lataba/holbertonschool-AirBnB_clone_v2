#!/usr/bin/python3
"""
Flask model for routes
Create a Flask web application instance
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Route function for the root URL ('/') """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def first():
    """ Route function for the root URL ('/hbnb') """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def second(text):
    """ Route function for the root URL ('/c/<text>') """
    txt = text.replace("_", " ")
    return f'C {txt}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
