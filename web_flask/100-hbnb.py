#!/usr/bin/python3
""" Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
    Required
        MUST use 'storage' for fetching data from the storage engine (File
        Storage or DBStorage) & remove the current session after each request
        routes: /hbnb: display a HTML page (borrowed from web_static)
                    and data from models.storage: State, City, Place &
                    Amenity sorted (A-Z)...
        MUST use the option 'strict_slashes=False in route definition
"""
from flask import Flask, render_template
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
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
@app.route('/hbnb')
def HBNB_view():
    """ Renders an HTML template listing all States, their cities
    Places and amenities therein """
    # get dict values from all() results
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User).values()
    # print('states: ', states)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places,
                           users=users)


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000, debug=True)
