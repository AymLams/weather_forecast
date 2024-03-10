from flask import Flask


def create_app():
    app = Flask(__name__)
    # We add the configuration from config.ini
    from config.ini_config import config_from_ini
    config_from_ini(app)
    from api.modules.weather.routes import bp_weather
    # We add the blueprint Weather to get the right path
    app.register_blueprint(bp_weather)

    return app