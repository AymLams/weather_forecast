#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
# Created By  : Aymeric Lamaallem
# version ='1.0'
# ---------------------------------------------------------------------------
""" Module to connect and launch the query on database """
# ---------------------------------------------------------------------------
import logging
import psycopg2
from flask import current_app


def fetchall_db(request: str):
    """
    Function to launch a query to our sql
    :param request:
    :return:
    """
    try:
        logging.info("Connecting to the database.")
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
