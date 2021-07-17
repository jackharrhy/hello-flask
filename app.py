import random
from flask import Flask

app = Flask(__name__)

def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route("/")
def route_hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def route_hello_name(name):
    return f"<p>Hello, {name}!</p>"

@app.route("/rainbow")
def rainbow():
    return f"""
<head>
    <style>
        body {{
            background-color: {random_color()};
        }}
    </style>
</head>
<body>
    <p>Rainbow Flask</p>
</body>
    """