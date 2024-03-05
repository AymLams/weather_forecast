# api.py
from flask import Flask
from modules.weather.routes import bp_weather
from config.ini_config import config_from_ini

app = Flask(__name__)
config_from_ini(app)

app.register_blueprint(bp_weather)

if __name__ == '__main__':
    app.run(debug=True)

