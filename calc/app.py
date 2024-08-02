# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your local host, Nick"

@app.route('/add')
def add_route():
    a = request.args.get('a', type = float)
    b = request.args.get('b', type = float)
    result = add(a, b)
    return str(result)

@app.route('/sub')
def subtract_route():
    a = request.args.get('a', type = float)
    b = request.args.get('b', type = float)
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def multiply_route():
    a = request.args.get('a', type = float)
    b = request.args.get('b', type = float)
    result = mult(a, b)
    return str(result)

@app.route('/div')
def divide_route():
    a = request.args.get('a', type = float)
    b = request.args.get('b', type = float)
    result = div(a, b)
    return str(result)

operators = {
    "add": add, "sub": sub, "mult": mult, "div": div,
}

@app.route("/math/<oper>")
def do_math(oper):
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
if __name__ == '__name__':
    app.run(debug=True)