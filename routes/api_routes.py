from flask import render_template, request, redirect, session
import requests

class ApiROutes:
    @staticmethod
    def configure_routes(app):

        @app.route("/food")
        def food():
            response = requests.get("https://api-mercurio.herokuapp.com/comida")
            dataJson = response.json()
            return render_template("food.html", dataJson = dataJson)

        @app.route("/cuadrimotosKids")
        def cuadrimotosKids():
            response = requests.get("https://api-mercurio.herokuapp.com/cuadrimotos")
            dataJson = response.json()
            option = "Infantil"
            return render_template("cuadrimotos.html", dataJson = dataJson, option = option)

        @app.route("/cuadrimotosAdults")
        def cuadrimotosAdults():
            response = requests.get("https://api-mercurio.herokuapp.com/cuadrimotos")
            dataJson = response.json()
            option = "Adulto"
            return render_template("cuadrimotos.html", dataJson = dataJson, option = option)

        @app.route("/opcionesCuadrimotos")
        def opcionesCuadrimotos():
            return render_template("opcionesCuadrimotos.html")

        @app.route("/restaurants")
        def restaurants():
            response = requests.get("https://api-mercurio.herokuapp.com/restaurante")
            dataJson = response.json()
            return render_template("restaurants.html", dataJson = dataJson)
