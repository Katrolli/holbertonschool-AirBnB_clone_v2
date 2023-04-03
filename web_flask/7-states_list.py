#!/usr/bin/python3
"""First flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
""" Flask app module"""


def close_storage(exception=None):
    storage.close()


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    close_storage(exception)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """ Route that prints hello """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    """ sa per siguri """
    app.run(host='0.0.0.0', port=5000, debug=True)
