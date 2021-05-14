from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hi")
def who():
    return "Who are you?"

@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"
