from flask import Flask, render_template
from models import storage
"""initialize the flask application"""
from models.state import State
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states():
    """Display a HTML page with a list of states"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """remove the current sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)