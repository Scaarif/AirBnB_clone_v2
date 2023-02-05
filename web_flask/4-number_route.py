#!/usr/bin/python3
""" Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
    Required
        routes: /:display "Hello HBNB!", /hbnb: display "HBNB" &
                /c/<text>: display "C" forllowed by 'text' variable (with any
                    underscores replaced by a space)
                /python/(<text>): display "Python" + what /c/<text> does...
                    with 'text' having the default value "is cool"
                /number/<n>: display "n is a number" ONLY IF n is an int
        MUST use the option 'strict_slashes=False in route definition
"""
from flask import Flask, escape

# instantiate a Flask application
app = Flask(__name__)
app.url_map.strict_slashes = False  # override default globally


# define a route to trigger the function defined right after
@app.route('/')
def hello_world():
    """ Returns 'Hello HBNB' """
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_world_2():
    """ Returns 'HBNB' """
    return "HBNB"


# the route captures a value (text) from the URL & passes to the function
@app.route('/c/<text>')
def hello_world_3(text):
    """ Returns 'C' followed by (space replaced underscores) text """
    return "C {}".format(escape(text).replace('_', ' '))


# route to trigger if no 'text' in url (defaults to defaults value)
@app.route('/python', defaults={'text': 'is cool'})
# route to trigger if 'text' in url
@app.route('/python/<text>')
def hello_world_4(text):
    """ Returns 'Python' followed by (space replaced underscores) text
    Note: <text> defaults to 'is cool' if undefined """
    return "Python {}".format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>')
def hello_number(n):
    """ returns "n is a number" if n is an int """
    return "{} is a number".format(n)


if __name__ == '__main__':
    # if run as an application (not module), listen on all public IPs
    app.run(host='0.0.0.0', port=5000)
