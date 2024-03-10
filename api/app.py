# app.py
from flask import Flask
from api.modules.weather.routes import bp_weather
from config.ini_config import config_from_ini

# We initiate or API with Flask
app = Flask(__name__)

# We add the configuration from config.ini
config_from_ini(app)

# We add the blueprint Weather to get the right path
app.register_blueprint(bp_weather)


# Main function launched to run the API
if __name__ == '__main__':
    app.run(debug=True)


