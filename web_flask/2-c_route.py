#!/usr/bin/python3
"""2. C is fun!"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    """Home route"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """hbnb route"""
    return "HBNB"


@app.route("/c/<string:text>")
def c_route(text):
    """c route"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
