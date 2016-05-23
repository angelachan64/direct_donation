from flask import Flask, render_template, session
from flask import redirect, url_for
from flask import request, session, redirect
import os.path
import users

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        print "POST"
        if "username" in request.form:
            username = request.form["username"]
            password = request.form["password"]
            user_id =  users.valid_login(username, password)
            if user_id >= 0:
                session["user"] = user_id
                redirect(url_for("home"))
            else:
                redirect(url_for("login"))
        elif "new_username" in request.form:
            print "CREATE"
            username = request.form["new_username"]
            password = request.form["new_password"]
            repeat = request.form["repeat"]
            email = request.form["email"]
            print "Values"
            creator = users.create_user(username, password, repeat, email)
            print creator
            if creator[0]:
                print "C[0]"
                session["user"] = users.valid_login(username, password)
                redirect(url_for("home"))
            else:
                print "C[1]"
                redirect(url_for("login"))
            
        
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == "GET":
        return render_template("payment.html")
    else:
        #THE INFO COLLECTED FOR PAYMENT
        session["name"] = request.form["name"]
        session["amount"] = request.form["amount"]
        session["email"] = request.form["email"]
        session["date"] = request.form["date"]
        users.make_donation(session["date"], session["name"], session["amount"], session["email"], 0)
        return redirect(url_for("transactions"))

    
@app.route("/transactions")
def transactions():
    n = session["name"]
    a = session["amount"]
    e = session["email"]
    d = session["date"]
    return render_template("transactions.html", 
                           name=n,
                           amount=a,
                           email=e,
                           date=d)
    

if __name__ == "__main__":
   app.debug = True
   app.secret_key = "lmaooooo"
   app.run('0.0.0.0', 8080 if os.path.isfile('./cloudy') else 8000)
