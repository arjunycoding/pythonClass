from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    print(request.args["name"])
    return f"<h1>Hello {request.args['name']}</h1>"

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {name}!"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}!"

@app.route("/add/<string:a>/<string:b>")
def adds(a, b):
    return f"{b} + {a} = {b + a}!"

@app.route("/string/<string:s>")
def string(s):
    return f"You said the string {s}!"

@app.route("/path/<path:p>")
def path(p):
    return f"You said the path {p}"