from .current_weather import current_weather
from .forecast_weather import forecast_weather
from flask import Blueprint

bp_weather = Blueprint('weather', __name__, url_prefix="/weather")


@bp_weather.route("/current", methods=["GET"])
def get_current_weather():
    return "Hello World"
    #return current_weather()


@bp_weather.route("/forecast", methods=["GET"])
def get_forecast_weather():
    return "Hello World"
    #return forecast_weather()