#!/usr/bin/python3
""" Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
    Required
        MUST use 'storage' for fetching data from the storage engine (FileStorage
            or DBStorage) & remove the current session after each request
        routes: /:display "Hello HBNB!"
        MUST use the option 'strict_slashes=False in route definition
"""
from flask import Flask, render_template
from models import storage
from models.state import State

# instantiate a Flask application
app = Flask(__name__)
app.url_map.strict_slashes=False  # override default globally

# function to remove current SQLAlchemy Session after each request
@app.teardown_appcontext
def close_context(self):
    """ tears down/removes current SQLAlchemy Session """
    storage.close()


# define a route to trigger the function defined right after
@app.route('/states_list')
def states_list():
    """ Renders an HTML template with all the States """
    # get dict values from all() results
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000, debug=True)
