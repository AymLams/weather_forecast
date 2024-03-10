from .weather import get_forecast_weather, get_current_weather
from flask import Blueprint
from flask import request

# We set our specific blueprint in order to have a well organised API
bp_weather = Blueprint('weather', __name__, url_prefix="/weather")


# We set the Path /weather/current
@bp_weather.route("/current", methods=["GET"])
def current_weather():
    # We get back the location parameter from the URL
    location = request.args.get("location", default="")
    return get_current_weather(location)


@bp_weather.route("/forecast", methods=["GET"])
def forecast_weather():
    # We get back the location parameter from the URL
    location = request.args.get("location", default="")
    return get_forecast_weather(location)
