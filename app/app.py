from flask import Flask
from app import views

app = Flask(__name__)

app.add_url_rule("/", view_func=views.index)
app.add_url_rule("/plain", view_func=views.plain)
