#!/usr/bin/python3
"""First flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
""" Flask app module"""


@app.teardown_appcontext
def closure():
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    """ Route that prints hello """
    states = storage.all(State)
    return render_template('states_list.html', states=states)


if __name__ == '__main__':
    """ sa per siguri """
    app.run(host='0.0.0.0', port=5000, debug=True)
