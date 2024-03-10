#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
# Created By  : Aymeric Lamaallem
# version ='1.0'
# ---------------------------------------------------------------------------
""" Module to test the forecast weather API """
# ---------------------------------------------------------------------------
from api import create_app
import json


def test_missing_location():
    """
    Function to test the behavior of our Forecast Weather API when it's missing the location parameter
    """
    app = create_app()
    client = app.test_client()

    response = client.get("/weather/current")
    assert response.status_code == 401
    assert b'Missing parameter' in response.data


def test_current():
    """
    FUnction to check the output of our Forecast Weather output
    """
    app = create_app()
    client = app.test_client()

    response = client.get("/weather/current?location=Toulouse")
    assert response.status_code == 200
    assert "relative_humidity" in json.loads(response.data).keys()
    assert "temperature" in json.loads(response.data).keys()
    assert "weather_description" in json.loads(response.data).keys()
    assert "wind_speed" in json.loads(response.data).keys()

