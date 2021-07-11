from flask import Flask
from routes.main_routes import MainRoutes
from routes.register_routes import RegisterRoutes
from routes.logprocess_routes import LogProcessRoutes
from routes.dashboard_routes import DashboardRoutes

app = Flask(__name__)
app.secret_key = "6LfEqg4bAAAAAHQCjHfFh4QeMmha2AKR0V2E99qO+"
MainRoutes.configure_routes(app)
RegisterRoutes.configure_routes(app)
LogProcessRoutes.configure_routes(app)
DashboardRoutes.configure_routes(app)


if __name__ == "__main__":
    app.run(debug=True)
