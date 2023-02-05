#!/usr/bin/python3
""" Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
    Required
        MUST use 'storage' for fetching data from the storage engine (File
        Storage or DBStorage) & remove the current session after each request
        routes: /states:display a HTML page with States(H1) and a (UL) of
                    sorted (A-Z) states
                /states/<id>: display a HTML page with (H1) State, (H3)
                    Cities and (UL)cities(sorted A-Z) if state with id exists
        MUST use the option 'strict_slashes=False in route definition
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

# instantiate a Flask application
app = Flask(__name__)
app.url_map.strict_slashes = False  # override default globally

# function to remove current SQLAlchemy Session after each request


@app.teardown_appcontext
def close_context(self):
    """ tears down/removes current SQLAlchemy Session """
    storage.close()


# define a route to trigger the function defined right after
@app.route('/states')
def states():
    """ Renders an HTML template listing all States """
    # get dict values from all() results
    states = storage.all(State).values()
    # print('states: ', states)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def state_and_cities(id):
    """ Renders an HTML template listing State(of <id>) cities """
    # get dict values from all() results
    states = storage.all(State).values()
    # print('id -> ', id)
    for state in states:
        if state.id == id:
            state = state
            break
    else:
        state = ''
    # print('states: ', states)
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000, debug=True)
