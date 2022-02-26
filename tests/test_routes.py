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
