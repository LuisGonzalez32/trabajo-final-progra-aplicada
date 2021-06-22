from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_cors import CORS, cross_origin
from logic.user_logic import UserLogic
import requests
import bcrypt

app = Flask(__name__)
app.secret_key = "Bad1secret2key3!+"
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # session.pop("loggedIn")
    if session.get("loggedIn"):
        # user = session.get("login_user")
        print(session.get("loggedIn"))
        return render_template("dashboard.html")  # , user=user)
    else:
        return redirect("logIn")


@app.route("/adminDashboard")
def adminDashboard():
    return render_template("adminDashboard.html")


@app.route("/rooms")
def rooms():
    return render_template("rooms.html")


@app.route("/logIn", methods=["GET", "POST"])
def logIn():
    if request.method == "GET":
        return render_template("logIn.html")
    elif request.method == "POST":
        session["loggedIn"] = False
        logic = UserLogic()
        user = request.form["user"]
        passwd = request.form["passwd"]
        userDict = logic.getUser(user)

        if userDict == []:
            return redirect("logIn")

        salt = userDict["salt"].encode("utf-8")
        hashPasswd = bcrypt.hashpw(passwd.encode("utf-8"), salt)
        dbPasswd = userDict["password"].encode("utf-8")

        if hashPasswd == dbPasswd:

            role = userDict["role"]
            if role == "client":
                session["loggedIn"] = True
                return redirect("dashboard")
            else:
                return redirect("adminDashboard")


@app.route("/createAccount", methods=["GET", "POST"])
def createAccount():
    data = {}
    if request.method == "GET":
        return render_template("createAccount.html")
    elif request.method == "POST":
        logic = UserLogic()
        userName = request.form["username"]
        passwd = request.form["passwd"]
        confpasswd = request.form["confpasswd"]
        if passwd == confpasswd:
            salt = bcrypt.gensalt(rounds=14)
            strSalt = salt.decode("utf-8")
            encPasswd = passwd.encode("utf-8")
            hashPasswd = bcrypt.hashpw(encPasswd, salt)
            strPasswd = hashPasswd.decode("utf-8")

            data["secret"] = "6LfEqg4bAAAAAHQCjHfFh4QeMmha2AKR0V2E99qO"
            data["response"] = request.form["g-recaptcha-response"]
            response = requests.post(
                "https://www.google.com/recaptcha/api/siteverify", params=data
            )
            if response.status_code == 200:
                messageJson = response.json()
                print(messageJson)
                if messageJson["success"]:
                    rows = logic.insertUser(userName, strPasswd, strSalt)
                    return redirect("logIn")

        return render_template("createAccount.html")


@app.route("/loginMenu")
def loginMenu():
    return render_template("loginMenu.html")


@app.route("/dateBooking")
def dateBooking():
    return render_template("dateBooking.html")


@app.route("/clientMenu")
def clientMenu():
    return render_template("clientMenu.html")


@app.route("/adminMenu")
def adminMenu():
    return render_template("adminMenu.html")


@app.route("/checkCapacity")
def checkCapacity():
    return render_template("checkCapacity.html")


@app.route("/myReservations")
def myReservations():
    return render_template("myReservations.html")


@app.route("/landingPage")
def landingPage():
    return render_template("landingPage.html")


@app.route("/food")
def food():
    return render_template("food.html")


@app.route("/foodTable")
def foodTable():
    return render_template("foodTable.html")


@app.route("/instalaciones")
def instalaciones():
    return render_template("instalaciones.html")


@app.route("/logout")
def logout():
    if session.get("loggedIn"):
        session.pop("loggedIn")
        return redirect("logIn")
    else:
        return redirect("logIn")


if __name__ == "__main__":
    app.run(debug=True)
