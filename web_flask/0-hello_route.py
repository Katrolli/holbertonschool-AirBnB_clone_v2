#!/usr/bin/python3
from flask import Flask
"""First flask app"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Route that prints hello """
    return "Hello HBNB!"


if __name__ == '__main__':
    """ sa per siguri """
    app.run(host='0.0.0.0', port=5000, debug=True)
