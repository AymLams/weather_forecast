# api.py
from current_weather import current_weather
from flask import Flask

app = Flask(__name__)


@app.route("/weather/current", methods=["GET"])
def get_current_weather():
    #return "Hello World"
    return current_weather()


@app.route("/weather/forecast", methods=["GET"])
def get_forecast_weather():
    return "Hello World"
    #return forecast_weather()


if __name__ == '__main__':
    app.run(debug=True)
