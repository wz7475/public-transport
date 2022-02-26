from app.api_model import StopsCollection
from app.app import app
import psycopg2


def test_base_route():
    client = app.test_client()
    url = "/plain"
    response = client.get(url)
    assert response.get_data() == b"plain text"
    assert response.status_code == 200


def test_model():
    stops = StopsCollection()
    pass


def test_db():
    con = psycopg2.connect(
        host="localhost",
        database="sample_db",
        user="postgres",
        password="123",
    )

    cur = con.cursor()

    cur.execute("SELECT * FROM example")
    pass
    rows = cur.fetchall()
    pass

def test_db_heroku():
    con = psycopg2.connect(
        host="ec2-52-208-185-143.eu-west-1.compute.amazonaws.com",
        database="dcdj3481fvgeod",
        user="xdnuuualruonmz",
        password="863cbcf255118bfcce20d2f1ff965afe13f198de97e3acc916f909c6f2ccf693",
    )

    cur = con.cursor()

    cur.execute("SELECT * FROM example")
    pass
    rows = cur.fetchall()
    pass
