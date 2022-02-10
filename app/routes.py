from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from .app import app
from .api_model import get_stops_data


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/delete")
def delete():
    return get_stops_data("app/config.json")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    return "<h3>Update task</h3>"
