from api import create_app
import json


def test_missing_location():
    app = create_app()
    client = app.test_client()

    response = client.get("/weather/current")
    assert response.status_code == 401
    assert b'Missing parameter' in response.data


def test_forecast():
    app = create_app()
    client = app.test_client()

    response = client.get("/weather/forecast?location=Toulouse")
    assert response.status_code == 200
    assert "general_evolution" in json.loads(response.data).keys()
    assert "mean_wind" in json.loads(response.data).keys()
    assert "tendance_temp" in json.loads(response.data).keys()
    assert "tendance_pres" in json.loads(response.data).keys()
