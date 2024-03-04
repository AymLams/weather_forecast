# api.py
from api.modules.weather.current_weather import current_weather
from flask import Flask

app = Flask(__name__)
config_from_ini(app)

if __name__ == '__main__':
    app.run(debug=True)

