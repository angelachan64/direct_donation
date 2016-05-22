from flask import Flask, render_template, session
from flask import redirect, url_for
import os.path

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
   app.debug = True
   app.secret_key = "lmaooooo"
   app.run('0.0.0.0', 8080 if os.path.isfile('./cloudy') else 8000)
