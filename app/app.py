from flask import Flask
from flask_cors import CORS

from app import views

app = Flask(__name__)
CORS(app)

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/plain", view_func=views.plain)
app.add_url_rule("/data", view_func=views.data)
app.add_url_rule("/timetable", view_func=views.timetable)
app.add_url_rule("/timetable_json", view_func=views.timetable_json)
