#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
# Created By  : Aymeric Lamaallem
# version ='1.0'
# ---------------------------------------------------------------------------
""" Module to create some jobs to our configuration """
# ---------------------------------------------------------------------------
import os
import configparser
import logging


def config_from_ini(app):
    """
    Configure Flask from an INI file
    Parameters:
        app         - Flask application instance
        config_file - Path to the configuration file (INI format)
        section     - Section name to load key/values from
    """
    config_file = os.path.join(os.path.dirname(__file__), 'config.ini')
    logging.debug('Loading Flask configuration from %s' % config_file)
    config = configparser.ConfigParser()
    config.read(config_file)
    flask_config = dict(config)
    for cfg_key in flask_config:
        app.config[cfg_key.upper()] = flask_config[cfg_key]