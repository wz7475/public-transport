from flask import Flask

from app.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = "/plain"

    response = client.get(url)
    assert response.get_data() == b"plain text"
    assert response.status_code == 200
