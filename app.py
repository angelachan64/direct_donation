from flask import Flask, render_template, session
from flask import redirect, url_for
from flask import request, session, redirect
import os.path

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")
    
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method=="GET":
        return render_template("payment.html")
    else:
        #THE INFO COLLECTED FOR PAYMENT
        session["name"] = request.form["name"]
        session["amount"] = request.form["amount"]
        session["email"] = request.form["email"]
        session["date"] = request.form["date"]
        return redirect(url_for("transactions"))

@app.route("/transactions")
def transactions():
    n = session["name"]
    a = session["amount"]
    e = session["email"]
    d = session["date"]
    return render_template("transactions.html", 
                           name = n,
                           amount = a,
                           email = e,
                           date = d
                       )
    


if __name__ == "__main__":
   app.debug = True
   app.secret_key = "lmaooooo"
   app.run('0.0.0.0', 8080 if os.path.isfile('./cloudy') else 8000)
