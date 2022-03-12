import json

import psycopg2
from flask import render_template

from app.api_model import FilteredStopsCollection
from app.config_db import cur


def index():
    return render_template("index.html")


# # @app.route("/delete")
# def delete():
#     return get_stops_data("app/config.json")


# # @app.route("/update/<int:id>", methods=["GET", "POST"])
# def update(id):
#     return "<h3>Update task</h3>"


# @app.route("/plain")
def plain():
    return "plain text"


def data():
    con = psycopg2.connect(
        host="ec2-52-208-185-143.eu-west-1.compute.amazonaws.com",
        database="dcdj3481fvgeod",
        user="xdnuuualruonmz",
        password="863cbcf255118bfcce20d2f1ff965afe13f198de97e3acc916f909c6f2ccf693",
    )

    cur = con.cursor()

    cur.execute("SELECT * FROM example")

    rows = cur.fetchall()

    return str(rows)


def timetable():
    cur.execute("SELECT * FROM bus_stops")
    stops_list = cur.fetchall()

    cur.execute("SELECT * FROM api_key")
    api_key = cur.fetchall()[0][0]
    stops = FilteredStopsCollection(api_key, stops_list)
    mytimetable = stops.get_timetable()
    output = ""
    elements = []
    for row in mytimetable:
        output += f"{str(row[0])} {row[1]} {row[2]}"
        elements.append(f"{str(row[0])} {row[1]} {row[2]}")
    return render_template("timetable.html", elements=elements)


def timetable_json():
    cur.execute("SELECT * FROM bus_stops")
    stops_list = cur.fetchall()

    cur.execute("SELECT * FROM api_key")
    api_key = cur.fetchall()[0][0]
    stops = FilteredStopsCollection(api_key, stops_list)
    mytimetable = stops.get_timetable()
    list_for_json = []
    for row in mytimetable:
        list_for_json.append([str(row[0]), row[1], row[2]])
    return json.dumps(list_for_json)
