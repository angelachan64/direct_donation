from flask import Flask, render_template, session
from flask import redirect, url_for
from flask import request, session, redirect
import os.path
from os import urandom
import users
import paypal

app = Flask(__name__)
indexfile = os.path.join(os.path.dirname(__file__), "index.html")
loginfile = os.path.join(os.path.dirname(__file__), "login.html")
homefile = os.path.join(os.path.dirname(__file__), "home.html")

@app.route("/")
def index():
    session["user"] = -1
    print indexfile
    return render_template(indexfile)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template(loginfile)
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
                return render_template(loginfile,
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
                return render_template(loginfile, signuperr=creator[1])


@app.route("/home")
def home():
    if "user" in session and session["user"] > -1:
        l = users.get_paypal_info(session["user"])
        tabler = paypal.getPaypalInfo(l[0], l[1], l[2])
        tabler += users.get_donation(session["user"])
        return render_template(homefile, data_table=tabler)
    else:
        return render_template(loginfile, loginerr="Please login first!")


@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if "user" in session and session["user"] > -1:
        if request.method == "GET":
            return render_template("payment.html")
        else:
            #THE INFO COLLECTED FOR PAYMENT
            fname = request.form["fname"]
            lname = request.form["lname"]
            ctype = request.form["ctype"]
            status = request.form["complete"]
            address = request.form["address"]
            amount = request.form["amount"]
            owner = request.form["owner"]
            date = request.form["date"]
            email = request.form["email"]
            paytype = request.form["paytype"]
            users.make_donation(fname, lname, ctype, status, address, amount, owner, date, email, paytype, session["user"])
            return redirect(url_for("home"))
    else:
        return render_template(loginfile, loginerr="Please login first!")

if __name__ == "__main__":
    app.debug = True
    app.secret_key = urandom(32)
    app.run('0.0.0.0', 8080 if os.path.isfile('./cloudy') else 8000)
    #app.run()
