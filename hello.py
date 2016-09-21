# Import Flask class from flask module
from flask import Flask
import random
# New Flask object 
app = Flask(__name__)

STYLE = "<style>body{margin:1em auto;max-width:40em;padding:0 .62em;font:1.2em/1.62em sans-serif;}h1,h2,h3{line-height:1.2em;}@media print{body{max-width:none}}</style>\n"

# Associate route to fxn
@app.route("/")
def hola():
    return STYLE + '''<h1>Welcome to the Main Page!</h1><hr>
<a href=about>About</a><br>
<a href=random>Random</a>
'''

@app.route("/about")
def about():
    return STYLE + '''Made with Flask<br>
By Seiji Yawata <hr>
<a href=..>Go Back</a>'''

@app.route("/random")
def info():
    dice = random.randint(1,6)
    return STYLE + "You rolled a " + str(dice) + '''<hr>
<a href=..>Go Back</a>'''

if __name__ == '__main__':
    app.run()


