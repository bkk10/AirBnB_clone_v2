#!/usr/bin/python3
"""Starts a simple Flask web application with one route"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a simple greeting"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
