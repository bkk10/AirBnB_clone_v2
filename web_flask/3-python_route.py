#!/usr/bin/python
"""Initialize the Flask application."""
from flask import Flask
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a simple greeting."""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return hbnb."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """return c followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "C {}".format(text)

@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Return python followed by the value of the text varialble"""
    text = text.replace('_',' ')
    return "Python {}".format(text)