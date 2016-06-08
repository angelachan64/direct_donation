from flask import Flask, render_template, session
from flask import redirect, url_for
from flask import request, session, redirect
import os.path
import users
import paypal

app = Flask(__name__)

@app.route("/")
def index():
    session["user"] = -1
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
                return redirect(url_for("home"))
            else:
                return render_template("login.html",
                                       loginerr="Incorrect Username or Password")
        elif "new_username" in request.form:
            print "CREATE"
            username = request.form["new_username"]
            password = request.form["new_password"]
            repeat = request.form["repeat"]
            email = request.form["email"]
            ppun = request.form["ppun"]
            ppp = request.form["ppp"]
            ppsig = request.form["ppsig"]
            print "Values"
            creator = users.create_user(username, password, repeat, email,
                                        ppun, ppp, ppsig)
            print creator
            if creator[0]:
                print "C[0]"
                session["user"] = users.valid_login(username, password)
                return redirect(url_for("home"))
            else:
                print "C[1]"
                return render_template("login.html", signuperr=creator[1])


@app.route("/home")
def home():
    if "user" in session and session["user"] >= -1:
        print users.get_donation(session["user"])
        #return render_template("home.html", data_table=users.get_donation(session["user"]))
        return render_template("home.html", data_table=paypal.getStatsHTMLTable())
    else:
        return render_template("login.html", loginerr="Please login first!")


@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if "user" in session and session["user"] >= -1:
        if request.method == "GET":
            return render_template("payment.html")
        else:
            #THE INFO COLLECTED FOR PAYMENT
            fname = request.form["fname"]
            lname = request.form["lname"]
            amount = request.form["amount"]
            email = request.form["email"]
            date = request.form["date"]
            users.make_donation(date, fname + " " + lname, amount, email, session["user"])
            return redirect(url_for("transactions"))
    else:
        return render_template("login.html", loginerr="Please login first!")

    
@app.route("/transactions")
def transactions():
    n = session["name"]
    a = session["amount"]
    e = session["email"]
    d = session["date"]
    os = session["orgs"]
    od = session["org_id"]
    
    return render_template("transactions.html",
                           name=n,
                           amount=a,
                           email=e,
                           date=d,
                           orgs=os,
                           org_id=od)


if __name__ == "__main__":
    app.debug = True
    app.secret_key = "lmaooooo"
    app.run('0.0.0.0', 8080 if os.path.isfile('./cloudy') else 8000)
