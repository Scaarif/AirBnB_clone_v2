#!/usr/bin/python3
""" Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
    Required
        MUST use 'storage' for fetching data from the storage engine (File
        Storage or DBStorage) & remove the current session after each request
        routes: /hbnb_filters: display a HTML page (borrowed from web_static)
                    and data from models.storage: State, City & Amenity
                    sorted (A-Z)...
        MUST use the option 'strict_slashes=False in route definition
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

# instantiate a Flask application
app = Flask(__name__)
app.url_map.strict_slashes = False  # override default globally

# function to remove current SQLAlchemy Session after each request


@app.teardown_appcontext
def close_context(self):
    """ tears down/removes current SQLAlchemy Session """
    storage.close()


# define a route to trigger the function defined right after
@app.route('/hbnb_filters')
def HBNB_filters():
    """ Renders an HTML template listing all States, their cities and
    amenities therein """
    # get dict values from all() results
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    # print('states: ', states)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000, debug=True)
