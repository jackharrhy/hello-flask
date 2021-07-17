from flask import Flask

app = Flask(__name__)

@app.route("/")
def route_hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def route_hello_name(name):
    return f"<p>Hello, {name}!</p>"
