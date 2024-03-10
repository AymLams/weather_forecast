#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
# Created By  : Aymeric Lamaallem
# version ='1.0'
# ---------------------------------------------------------------------------
""" Module to test the current weather API """
# ---------------------------------------------------------------------------
from api import create_app
import json


def test_missing_location():
    """
    Function to test the behavior of the current weather API when we do not have the location
    """
    app = create_app()
    client = app.test_client()

    response = client.get("/weather/current")
    assert response.status_code == 401
    assert b'Missing parameter' in response.data


def test_forecast():
    """
    Function to test the output of our current Weather API
    """
    app = create_app()
    client = app.test_client()

    response = client.get("/weather/forecast?location=Toulouse")
    assert response.status_code == 200
    assert "general_evolution" in json.loads(response.data).keys()
    assert "mean_wind" in json.loads(response.data).keys()
    assert "tendance_temp" in json.loads(response.data).keys()
    assert "tendance_pres" in json.loads(response.data).keys()
