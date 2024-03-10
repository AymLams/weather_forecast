from api import create_app
import json


def test_missing_location():
    app = create_app()
    client = app.test_client()

    response = client.get("/weather/current")
    assert response.status_code == 401
    assert b'Missing parameter' in response.data


def test_current():
    app = create_app()
    client = app.test_client()

    response = client.get("/weather/current?location=Toulouse")
    assert response.status_code == 200
    assert "relative_humidity" in json.loads(response.data).keys()
    assert "temperature" in json.loads(response.data).keys()
    assert "weather_description" in json.loads(response.data).keys()
    assert "wind_speed" in json.loads(response.data).keys()

