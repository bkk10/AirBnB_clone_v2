#!/usr/bin/python
"""Starts a Flask web application with a route to display cities by states."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a page with states, amenities and cities"""
    state = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenitites = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    return render_template("10-hbnb_filters.html", states=state, amenities=amenitites)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)