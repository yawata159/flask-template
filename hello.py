# Import Flask class from flask module
from flask import Flask

# New Flask object 
app = Flask(__name__)

# Associate route to fxn
@app.route("/")
def hola():
    return "Hello!"


@app.route("/about")
def about():
    return "This is the about page"

@app.route("/info")
def info():
    return "This is the info page."

@app.route("/credits")
def credits():
    return "This is the credits page."

if __name__ == '__main__':
    app.run()


