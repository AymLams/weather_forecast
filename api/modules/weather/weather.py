from utils.count import too_many_count, check_count_per_day
from utils.compute_weather import *
import requests
from flask import current_app, jsonify
import json


def get_forecast_weather(location: str):
    """
    Function to return the forecast of the weather depending on the location
    """

    if location:
        params = {
            "city": location,
            "days": "7",
            **current_app.config["API_WEATHER_PARAMS"]
        }
        result = requests.get(current_app.config["API_WEATHER"]["forecast_url"], params)

        if result.status_code == 200:
            count, success = check_count_per_day()
            if success:
                if count:
                    return get_forecast_weather_data(json.loads(result.content)["data"])
                else:
                    return too_many_count()
            else:
                return jsonify({"error": "Error with the database"}), 501
        else:
            return result.message, result.status_code
    else:
        return jsonify({"error": "Missing parameter 'location'."}), 401


def get_current_weather(location: str):
    """
    Function qui retourne la météo actuelle
    :return:
    """
    if location:
        params = {
            "city": location,
            **current_app.config["API_WEATHER_PARAMS"]
        }
        result = requests.get(current_app.config["API_WEATHER"]["current_url"], params)

        if result.status_code == 200:
            count, success = check_count_per_day()
            if success:
                if count:
                    return get_current_weather_data(json.loads(result.content)["data"][0])
                else:
                    return too_many_count()
            else:
                return jsonify({"error": "Error with the database"}), 501
        else:
            return jsonify({"error": str(result.text)}), result.status_code
    else:
        return jsonify(json.dumps({"error": "Missing parameter 'location'."})), 401


def get_current_weather_data(data):
    """
    Function to build our output from the Data we get back from the Weather API
    """
    output = {
        "location": data["city_name"],
        "weather_description": data["weather"]["description"],
        "temperature": data["temp"],
        "wind_speed": convert_mpers_2_kmperh(data["wind_spd"]),
        "relative_humidity": data["rh"]
    }

    return jsonify(output), 200


def get_forecast_weather_data(data):
    """
    Function to build our output for the forecast using the output from the Weather API
    Warning: compare to the current weather, here we have a list of 7 elements
    """
    # We initialize our different variables needed
    temp, pres, pop, wind_speed = [], [], [], []

    # We set the content of our variables using the data from the API
    for content in data:
        temp.append(content["temp"])
        pres.append(content["pres"])
        pop.append(content["pop"])
        wind_speed.append(content["wind_spd"])

    output = {
        "general_evolution": compute_general_evolution(temp, pres, pop),
        "tendance_temp": compute_tendance(temp),
        "tendance_pres": compute_tendance(pres),
        "mean_wind": compute_mean_wind(wind_speed)
    }
    return jsonify(output), 200
