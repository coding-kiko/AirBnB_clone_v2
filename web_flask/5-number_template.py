#!/usr/bin/python3
"""starts flask web app"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def home():
    """home route"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "hbnb route"
    return ("Hello HBNB!")


@app.route('/c/<text>', strict_slashes=False)
def c_is_etc(text):
    """variable route"""
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def python_is_etc(text="is cool"):
    """variable route"""
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<n>', strict_slashes=False)
def reps_int(n):
    """variable route"""
    try:
        n = int(n)
        return ("{} is a number".format(n))
    except:
        pass


@app.route('/number_template/<n>', strict_slashes=False)
def templates(n):
    """displays html page only if n is an int"""
    try:
        n = int(n)
        return (render_template('5-number.html', n=n))
    except:
        pass

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
