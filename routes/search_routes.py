from flask import render_template, request, redirect, session
from logic.user_logic import UserLogic
import bcrypt


class searchRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/search", methods=["POST"])
        def login():
            if request.method == "POST":
                search = request.post["search"]
                if search == "book a room":
                    return render_template("login.html")
