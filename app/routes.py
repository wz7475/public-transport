from flask import render_template
from .api_model import get_stops_data


def configure_routes(app):
    @app.route("/", methods=["POST", "GET"])
    def index():
        return render_template("index.html")

    @app.route("/delete")
    def delete():
        return get_stops_data("app/config.json")

    @app.route("/update/<int:id>", methods=["GET", "POST"])
    def update(id):
        return "<h3>Update task</h3>"

    @app.route("/plain")
    def plain():
        return "plain text"
