from flask import Flask
from app.api_model import StopsCollection
from app.app import app


def test_base_route():
    client = app.test_client()
    url = "/plain"
    response = client.get(url)
    assert response.get_data() == b"plain text"
    assert response.status_code == 200


def test_model():
    stops = StopsCollection()
    pass
