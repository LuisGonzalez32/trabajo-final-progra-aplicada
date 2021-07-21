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
            return render_template("dashboard.html")

        @app.route("/adminDashboard")
        def adminDashboard():
            return render_template("adminDashboard.html")

        @app.route("/clientMenu")
        def clientMenu():
            return render_template("clientMenu.html")

        @app.route("/adminMenu")
        def adminMenu():
            return render_template("adminMenu.html")

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
                    roomId = request.form["roomId"]

                    return render_template(
                        "dateBooking.html", userName=userName, roomId=roomId
                    )

        @app.route("/dateBooking", methods=["GET", "POST"])
        def dateBooking():
            if request.method == "GET":
                return render_template("dateBooking.html")
            if request.method == "POST":
                checkin = request.form["checkin"]
                checkout = request.form["checkout"]
                userName = request.form["userName"]
                roomId = request.form["roomId"]

                format = "%Y-%m-%dT%H:%M"
                checkin = datetime.datetime.strptime(checkin, format)
                checkout = datetime.datetime.strptime(checkout, format)

                rooms = logic.roomsBooked()
                roomId = int(roomId)
                y = False
                z = False

                if checkout > checkin:
                    if len(rooms) > 0:
                        for x in rooms:
                            if roomId is x["bookId"]:
                                z = True
                                if (checkout < x["checkin"]) or (
                                    checkin > x["checkin"] and checkin > x["checkout"]
                                ):
                                    y = True
                                else:
                                    return render_template("error.html")
                else:
                    return render_template("error.html")

                if z is False:
                    logic.bookRoom(userName, roomId, checkin, checkout)

                if y is True:
                    logic.bookRoom(userName, roomId, checkin, checkout)

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
            roomsBooked = logic.getRoomsBooked()
            if session["role"] == "client":
                return render_template(
                    "myReservations.html", userName=userName, roomsBooked=roomsBooked
                )
            elif session["role"] == "admin":
                return render_template("allReservations.html", roomsBooked=roomsBooked)

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

        @app.route("/bookEvent", methods=["GET", "POST"])
        def bookEvent():
            if request.method == "GET":
                return render_template("bookEvent.html")
            elif request.method == "POST":
                user = session["login_user"]
                eventName = request.form["eventName"]
                date = request.form["date"]
                quantity = request.form["quantity"]

                format = "%Y-%m-%dT%H:%M"
                date = datetime.datetime.strptime(date, format)

                events = logic.getAllEvents()
                y = True

                if len(events) > 0:
                    for x in events:
                        if date == x["date"]:
                            y = False
                            return render_template("error.html")
                else:
                    logic.insertEvent(eventName, user, date, quantity)
                    return render_template("dashboard.html")

                if y is True:
                    logic.insertEvent(eventName, user, date, quantity)
                    return render_template("dashboard.html")

        @app.route("/instalaciones")
        def instalaciones():
            return render_template("instalaciones.html")

        @app.route("/deleteRoom", methods=["POST"])
        def deleteRoom():
            if request.method == "POST":
                roomId = request.form["id"]
                logic.deleteRoomBooked(roomId)
                return render_template("dashboard.html")

        @app.route("/deleteEvent", methods=["POST"])
        def deleteEvent():
            if request.method == "POST":
                eventId = request.form["id"]
                logic.deleteEvent(eventId)
                return render_template("dashboard.html")

        @app.route("/eventTable")
        def eventTable():
            userName = session["login_user"]
            role = session["role"]
            events = logic.getAllEvents()
            if role == "client":
                return render_template(
                    "eventTable.html", userName=userName, events=events
                )
            elif role == "admin":
                return render_template("allEvents.html", events=events)

        @app.route("/logout")
        def logout():
            if session.get("loggedIn"):
                session.pop("loggedIn")
                return redirect("login")
            else:
                return redirect("login")

        if __name__ == "__main__":
            app.run(debug=True)
