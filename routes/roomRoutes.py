from flask import render_template, request, redirect, session
from logic.user_logic import UserLogic
import bcrypt
import datetime
import requests

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
                    roomPrice = request.form["roomPrice"]

                    return render_template(
                        "dateBooking.html", userName=userName, roomId=roomId, roomPrice=roomPrice
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
                price = int(request.form["roomPrice"])

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
                    logic.bookRoom(userName, price, roomId, checkin, checkout)


                if y is True:
                    logic.bookRoom(userName, price, roomId, checkin, checkout)


                name = session["login_user"]
                total = logic.getTotal(name)
                return render_template("dashboard.html", total = total)

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
            if session["role"] == "client":
                return render_template(
                    "myReservations.html", userName=userName, roomsBooked=roomsBooked
                )
            elif session["role"] == "admin":
                return render_template("allReservations.html", roomsBooked=roomsBooked)

        @app.route("/deleteRoom", methods=["POST"])
        def deleteRoom():
            if request.method == "POST":
                roomId = request.form["id"]
                logic.deleteRoomBooked(roomId)

                name = session["login_user"]
                total = logic.getTotal(name)
                return render_template("dashboard.html", total = total)

        @app.route("/puto")
        def puto():
            restapi     = "https://credit-card-auth-api-cerberus.herokuapp.com"
            endpoint    = "/verify"

            url = f"{restapi}{endpoint}"

            data = {
                "name": "Erick Hernandez",
                "number": "7000123456780000",
                "date": "12/24",
                "code": "182",
                "balance": 20.25 # el valor de la transaccion
            }

            response = requests.post(url, data=data)
            print(response)
            if response.status_code == 200:
                dataJson = response.json()
                if dataJson['response'] == '00':
                    return dataJson
                else:
                    return dataJson
