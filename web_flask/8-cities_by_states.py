#!/usr/bin/python
"""Starts a Flask web application with a route to display cities by states."""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a page with a list of cities by states"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template("8-cities_by_states.html", states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """remove the current sqlalchemy session"""
    storage.close()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
