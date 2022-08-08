from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
        <p>Hello world</p>
        <p><a href="/add">Go To Addition Calculator</a></p>
    """

@app.route("/greet/<name>")
def hello_name(name):
    return f"Hello, {name}!"


@app.route("/calculator", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        a = request.form.get("a", 0,  type=int)
        b = request.form.get("b", 0,  type=int)
        return f"{a} + {b} = {a + b}!"
    else:
        return """
            <form method="POST">
                <label for="form_a">First Number:</label>
                <input type="number" id="form_a" name="a"/>
                <br/>
                <br/>

                <label for="form_b">Second Number:</label>
                <input type="number" id="form_b" name="b"/>
                <br/>
                <br/>

                <input type="submit" value="Add"/>
            </form>
        """