from flask import render_template, request, redirect, session
from logic.user_logic import UserLogic
import bcrypt


class LogProcessRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "GET":
                return render_template("login.html")
            elif request.method == "POST":
                logic = UserLogic()
                username = request.form["user"]
                password = request.form["password"]
                userDict = logic.getUser(username)

                # validar si userDict no es vacio
                if len(userDict) != 0:
                    # user existe
                    salt = userDict["salt"].encode("utf-8")
                    strPassword = password.encode("utf-8")
                    hashPassword = bcrypt.hashpw(strPassword, salt)
                    dbPassword = userDict["password"].encode("utf-8")
                    if hashPassword == dbPassword:
                        # se valido la password, se puede crear sesion y pasar al dashboard
                        session["login_user"] = username
                        session["loggedIn"] = True

                        if userDict["role"] == "client":
                            session["role"] = "client"
                            return redirect("dashboard")

                        elif userDict["role"] == "admin":
                            session["role"] = "admin"
                            return redirect("adminDashboard")
                    else:
                        return redirect("login")
                else:
                    # user no existe
                    return redirect("login")

                return redirect("login")

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
