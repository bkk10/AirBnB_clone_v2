#!/usr/bin/python
"""Starts a Flask web application with a route to display cities by states."""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display a page with a list of cities by states"""
    city = sorted(storage.all("City").values(), key=lambda s: s.name)
    states = sorted(storage.all("State").values(), key=lambda s: s.name)
    return render_template("8-cities_by_states.py", states=states, city=city)

@app.teardown_appcontext
def teardown_db(exception):
    """remove the current sqlalchemy session"""
    storage.close()


