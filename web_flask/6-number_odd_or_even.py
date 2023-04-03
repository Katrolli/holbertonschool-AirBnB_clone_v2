#!/usr/bin/python3
"""First flask app"""
from flask import Flask, render_template

app = Flask(__name__)
""" Flask app module"""


@app.route("/", strict_slashes=False)
def hello():
    """ Route that prints hello """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Route that prints hello """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Route that prints hello """
    return "C {}".format(text.replace('_', " "))


@app.route("/python", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is_cool'):
    """ Route that prints hello """
    return "Python {}".format(text.replace('_', " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """ Route that prints hello """
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Route that prints hello """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """ Route that prints hello """
    mode = ''
    if n % 2 == 0:
        mode = "even"
    else:
        mode = "odd"
    return render_template('6-number_odd_or_even.html', n=n, mode=mode)


if __name__ == '__main__':
    """ sa per siguri """
    app.run(host='0.0.0.0', port=5000, debug=True)
