#!/usr/bin/python3
""" Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
    Required
        MUST use 'storage' for fetching data from the storage engine (File
        Storage or DBStorage) & remove the current session after each request
        routes: /:display "Hello HBNB!"
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
@app.route('/cities_by_states')
def states_and_their_cities():
    """ Renders an HTML template with all the States and their cities """
    # get dict values from all() results
    states = storage.all(State).values()
    # print('states: ', states)
    '''for state in states:
        state_city = state.cities
        print(type(state_city))
        if state_city:
            print('state_city: ', state_city)
            break
        else:
            print('state_city: ', 'None')
    else:
        print('not iterable?')'''
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000, debug=True)
