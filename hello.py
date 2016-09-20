# Import Flask class from flask module
from flask import Flask
import random
# New Flask object 
app = Flask(__name__)

# Associate route to fxn
@app.route("/")
def hola():
    return '''<h1>Welcome to the Main Page!</h1><hr>
<a href=about>About</a><br>
<a href=random>Random</a>
'''

@app.route("/about")
def about():
    return '''Made with Flask<hr>
<a href=..>Go Back</a>'''

@app.route("/random")
def info():
    dice = random.randin(1,6)
    return "You rolled a " + str(dice) + '''<hr>
<a href=..>Go Back</a>'''

if __name__ == '__main__':
    app.run()


