#!/usr/bin/python3
""" Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
    Required
        routes: /:display "Hello HBNB!"
        MUST use the option 'strict_slashes=False in route definition
"""
from flask import Flask

# instantiate a Flask application
app = Flask(__name__)


# define a route to trigger the function defined right after
@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns 'Hello HBNB' """
    return "Hello HBNB!"


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000, debug=True)
