#!/usr/bin/python3
""" script that starts a Flask web applicationn
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
              (replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """display C followed by the value of the text variable
    (replace underscore _ symbols with a space)"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
