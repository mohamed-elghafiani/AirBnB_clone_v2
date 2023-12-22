#!/usr/bin/python3
from flask import Flask, render_template

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
    return "C " + text.replace("_", " ")


@app.route("/python")
@app.route("/python/<text>")
def python_route(text="is cool"):
    """python route"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>")
def number_route(n):
    """number route"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """number template"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
