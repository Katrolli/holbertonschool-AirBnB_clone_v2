#!/usr/bin/python3
"""First flask app"""
from flask import Flask

app = Flask(__name__)
""" Flask app module"""


@app.route("/", strict_slashes=False)
def first_route():
    """ Route that prints hello """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def second_route():
    """ Route that prints hello """
    return "Hello!"


if __name__ == '__main__':
    """ sa per siguri """
    app.run(host='0.0.0.0', port=5000, debug=True)
