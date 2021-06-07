from flask import Flask, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/adminDashboard")
def adminDashboard():
    return render_template("adminDashboard.html")


@app.route("/rooms")
def rooms():
    return render_template("rooms.html")


@app.route("/loginMenu")
def loginMenu():
    return render_template("loginMenu.html")


@app.route("/logIn")
def logIn():
    return render_template("logIn.html")


@app.route("/createAccount")
def createAccount():
    return render_template("createAccount.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/aboutUs")
def aboutUs():
    return render_template("aboutUs.html")


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


if __name__ == "__main__":
    app.run(debug=True)
