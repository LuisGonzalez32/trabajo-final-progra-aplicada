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

        @app.route("/landingPage")
        def landingPage():
            return render_template("landingPage.html")

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

        if __name__ == "__main__":
            app.run(debug=True)
