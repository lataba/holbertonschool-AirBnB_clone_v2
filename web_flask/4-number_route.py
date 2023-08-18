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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def tirth(text='is cool'):
    """ Route function for the root URL ('/python/<text>') """
    txt = text.replace("_", " ")
    return f'Python {txt}'


@app.route('/number/<int:n>', strict_slashes=False)
def fourth(n):
    """ Route function for the root URL ('/number/<n>') """
    return f'{n} is a number'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
