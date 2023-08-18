#!/usr/bin/python3
"""
Flask model for routes
Create a Flask web application instance
"""

from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def tirth(text='is cool'):
    """ Route function for the root URL ('/python/<text>') """
    txt = text.replace("_", " ")
    return f'Python {txt}'


@app.route('/number/<int:n>', strict_slashes=False)
def fourth(n):
    """ Route function for the root URL ('/number/<n>') """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def fifth(n):
    """ Route function for the root URL ('/number_template/<n>') """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def sixth(n):
    """ Route function for the root URL ('/number_odd_or_even/<int:n') """
    if n % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"
    return render_template(
        '6-number_odd_or_even.html',
        num=n, val=odd_even
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
