from flask import render_template, request, redirect, session
from logic.user_logic import UserLogic
import bcrypt
import datetime

logic = UserLogic()

class RoomRoutes:
    @staticmethod
    def configure_routes(app):
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

                print(userName)
                print(roomId)

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
                            if roomId is x["roomId"]:
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
            roomsBooked = logic.roomsBooked()
            print(session["role"])
            if session["role"] == "client":
                return render_template(
                    "myReservations.html", userName=userName, roomsBooked=roomsBooked
                )
            elif session["role"] == "admin":
                return render_template("allReservations.html", roomsBooked=roomsBooked)
