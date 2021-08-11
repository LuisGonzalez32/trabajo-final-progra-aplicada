from flask import Flask, render_template, redirect, request, url_for, flash, session
import requests
from logic.user_logic import UserLogic
import datetime

logic = UserLogic()

class DashboardRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/dashboard")
        def dashboard():
                name = session["login_user"]
                total = logic.getTotal(name)
                return render_template("dashboard.html", total = total)

        @app.route("/adminDashboard")
        def adminDashboard():
            return render_template("adminDashboard.html")

        @app.route("/landingPage")
        def landingPage():
            return render_template("landingPage.html")

        @app.route("/checkout", methods=["GET", "POST"])
        def checkout():
            login_user = session["login_user"]
            total = logic.getTotal(login_user)
            if request.method == "GET":
                return render_template("checkout.html", total = total)
            if request.method == "POST":

                name = request.form["name"]
                creditCard = request.form["creditCard"]
                date = request.form["date"]
                code = request.form["code"]
                balance = request.form["total"]
                balance = int(balance)

                data = {
                    "name": name,
                    "number": creditCard,
                    "date": date,
                    "code": code,
                    "balance": 9
                }

                response = requests.post("http://credit-card-auth-api-cerberus.herokuapp.com/verify", data=data)
                print(response)
                if response.status_code == 200:
                    dataJson = response.json()
                    print(dataJson['response'])
                    if dataJson['response'] == '00':
                        delete = logic.deleteTotal(login_user)
                        print(delete)
                        if delete == 0:
                            return render_template("error.html")
                        else:
                            total = logic.getTotal(name)
                            print(total)
                            return render_template("dashboard.html", total = total)
                    else:
                        return render_template("error.html")
                else:
                    return render_template("error.html")




        @app.route("/instalaciones")
        def instalaciones():
            return render_template("instalaciones.html")

        @app.route("/logout")
        def logout():
            if session.get("loggedIn"):
                session.pop("loggedIn")
                return redirect("login")
            else:
                return redirect("login")

        @app.route("/error", methods=["GET", "POST"])
        def error():
            if request.method == "GET":
                return render_template("error.html")
            if request.method == "GET":
                return

        if __name__ == "__main__":
            app.run(debug=True)
