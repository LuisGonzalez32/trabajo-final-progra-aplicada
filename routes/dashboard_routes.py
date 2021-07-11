from flask import Flask, render_template, redirect, request, url_for, flash, session
import requests
from logic.user_logic import UserLogic


class DashboardRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/dashboard")
        def dashboard():
            return render_template("dashboard.html")

        @app.route("/adminDashboard")
        def adminDashboard():
            return render_template("adminDashboard.html")

        @app.route("/loginMenu", methods=["GET", "POST"])
        def loginMenu():
            if request.method == "GET":
                return render_template("loginMenu.html")
            elif request.method == "POST":
                user = request.form.getlist("logMenu")
                if user == ["register"]:
                    return render_template("register.html")
                elif user == ["login"]:
                    return render_template("login.html")

        @app.route("/clientMenu")
        def clientMenu():
            return render_template("clientMenu.html")

        @app.route("/adminMenu")
        def adminMenu():
            return render_template("adminMenu.html")

        logic = UserLogic()

        @app.route("/rooms", methods=["GET", "POST"])
        def rooms():
            if request.method == "GET":
                return render_template("rooms.html")
            elif request.method == "POST":
                user = request.form.getlist("checkCapacity", type=int)

                personArray = logic.getAllRooms()
                return render_template("rooms.html", persons=personArray, user=user)

        @app.route("/bookRoom", methods=["GET", "POST"])
        def bookRoom():
            if request.method == "GET":
                return render_template("checkCapacity.html")
            if request.method == "POST":
                if "roomId" in request.form:
                    userName = session["login_user"]
                    userDict = logic.getUser(userName)
                    roomId = request.form["roomId"]
                    userId = userDict.get("id")

                    return render_template(
                        "dateBooking.html", userId=userId, roomId=roomId
                    )

        @app.route("/dateBooking", methods=["GET", "POST"])
        def dateBooking():
            if request.method == "GET":
                return render_template("dateBooking.html")
            if request.method == "POST":
                checkin = request.form["checkin"]
                checkout = request.form["checkout"]
                userId = request.form["userId"]
                roomId = request.form["roomId"]

                # rooms = logic.getRoomsBooked()
                # for x in rooms.items():
                #    if checkin > x
                logic.bookRoom(userId, roomId, checkin, checkout)
                return render_template("dashboard.html")

        @app.route("/checkCapacity", methods=["GET", "POST"])
        def checkCapacity():
            if request.method == "GET":
                return render_template("checkCapacity.html")
            elif request.method == "POST":
                user = request.form["checkCapacity"]
                return render_template("checkCapacity.html", user=user)

        @app.route("/myReservations")
        def myReservations():
            userName = session["login_user"]
            print(type(userName))
            roomsBooked = logic.getRoomsBooked()
            # print(roomsBooked.checkout)
            return render_template(
                "myReservations.html", userName=userName, roomsBooked=roomsBooked
            )
            # else:
            # poner alert que no hay recervaciones
            # return render_template("dashboard.html")

        @app.route("/landingPage")
        def landingPage():
            return render_template("landingPage.html")

        @app.route("/food", methods=["GET", "POST"])
        def food():
            if request.method == "GET":
                return render_template("food.html")
            elif request.method == "POST":
                user = request.form.getlist("checkCapacity")
                return render_template("food.html")

        @app.route("/foodTable")
        def foodTable():
            return render_template("foodTable.html")

        @app.route("/instalaciones")
        def instalaciones():
            return render_template("instalaciones.html")

        @app.route("/deleteRoom", methods=["POST"])
        def deleteRoom():
            if request.method == "POST":
                roomId = request.form["id"]
                logic.deleteRoomBooked(roomId)
                return render_template("dashboard.html")

        @app.route("/logout")
        def logout():
            if session.get("loggedIn"):
                session.pop("loggedIn")
                return redirect("login")
            else:
                return redirect("login")

        if __name__ == "__main__":
            app.run(debug=True)
