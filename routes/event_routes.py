from flask import render_template, request, redirect, session
from logic.user_logic import UserLogic
import bcrypt
import datetime

logic = UserLogic()


class EventRoutes:
    @staticmethod
    def configure_routes(app):
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