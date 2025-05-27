#!/usr/bin/python3
"""Simple Flask app to display states and cities"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

# Close the storage session when the app context ends
@app.teardown_appcontext
def close_storage(error):
    storage.close()

# Route for showing all states or one state by ID
@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def show_states(id=None):
    all_states = storage.all(State).values()
    states = sorted(all_states, key=lambda state: state.name)

    if id:
        selected_state = None
        for state in states:
            if state.id == id:
                selected_state = state
                break
        return render_template("9-states.html", state=selected_state)
    else:
        return render_template("9-states.html", states=states)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
