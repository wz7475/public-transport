from flask import render_template
import psycopg2


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
