from api.modules.weather import bp
from current_weather import current_weather
from forecast_weather import forecast_weather

@bp.route("/current", methods=["GET"])
def get_current_weather():
    #return "Hello World"
    return current_weather()


@bp.route("/forecast", methods=["GET"])
def get_forecast_weather():
    return "Hello World"
    #return forecast_weather()