from solveRoute import solveRoute
import json

from flask import Flask

app = Flask(__name__)

places = [
    (50,0),
    (75,0),
    (25,10),
    (100,20),
    (0,50),
    (75,75),
    (50,100),
    (43,72),
    (12,44),
    (94,5)
]

@app.route("/")
def index():
    return json.dumps({'original': places, 'solved': solveRoute(places)})

# app.run(debug=True, port=8000, host="0.0.0.0")