import logging

import psycopg2
from flask import current_app
from flask import jsonify


def fetchall_db(request: str):
    """
    Function to launch a query to our sql
    :param request:
    :return:
    """
    try:
        # We make the connection to the database
        con = psycopg2.connect(
            database=current_app.config["DATABASE"]["name"],
            user=current_app.config["DATABASE"]["user"],
            password=current_app.config["DATABASE"]["password"],
            port=current_app.config["DATABASE"]["port"]
        )
        cursor = con.cursor()
        cursor.execute(request)
        result = cursor.fetchall()
        con.commit()
        cursor.close()
        return result, True

    except Exception as e:
        logging.error("Connection to the database impossible.")
        logging.error(e)
        return None, False


def connect_to_database():
    try:
        # Tentative de connexion à la base de données PostgreSQL
        connection = psycopg2.connect(
            database=current_app.config["DATABASE"]["name"],
            user=current_app.config["DATABASE"]["user"],
            password=current_app.config["DATABASE"]["password"],
            port=current_app.config["DATABASE"]["port"]
        )
        connection.close()
    except Exception as e:
        # En cas d'erreur de connexion, renvoyer une erreur HTTP 503 (Service Unavailable)
        logging.error("Erreur lors de la connexion à la base de données : %s", str(e))
        response = jsonify({"error": "La base de données n'est pas accessible."})
        response.status_code = 503
        return response
