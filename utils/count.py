#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*- Line 2
# ----------------------------------------------------------------------------
# Created By  : Aymeric Lamaallem
# version ='1.0'
# ---------------------------------------------------------------------------
""" Module to act on the count of connection per day: Get count,
    Create count, Update count """
# ---------------------------------------------------------------------------
from .database import fetchall_db
from flask import current_app, jsonify


def get_count_per_day():
    """
    Function to get the current count of connection for today
    """
    # We create the query
    sql_request = f"SELECT count FROM {current_app.config['COUNT']['table_name']} WHERE date = CURRENT_DATE"
    # We launch the connection to our sql
    count, success = fetchall_db(sql_request)

    # We check if we didn't have any issue on the request
    if success:
        # We return 0 if there is no connection for today else the current count
        if count:
            return count[0][0]
        else:
            return 0
    else:
        return success


def check_count_per_day():
    """
    Function to check if we already have too many connections for today on our api
    """

    # We get back the count of connection for today
    count = get_count_per_day()

    # If no connection
    if count == 0:
        # We create the row in sql and we return True
        success = create_count()
        return True, success

    # If less than 50 connections
    elif count < int(current_app.config['COUNT']['count_total_per_day']):
        # We update the count and we return True
        success = update_count()
        return True, success

    # More than 50 connections
    elif count >= int(current_app.config['COUNT']['count_total_per_day']):
        # We return False
        return False, True

    # We had an issue by trying to get the number of count for today
    else:
        return None, False


def update_count():
    """
    We update the count of connection for today with a +1
    :return: Boolean of success
    """
    # SQL Update query to set the count to +1
    sql_request = f"UPDATE {current_app.config['COUNT']['table_name']} " \
                  f"SET count = count + 1 WHERE date = CURRENT_DATE RETURNING *;"
    # We launch and run the sql query
    count, success = fetchall_db(sql_request)
    # We return the state
    return success


def create_count():
    """
    We create the first connection of the day
    :return: Boolean of success
    """
    # We make the query to insert the first count of the day
    sql_request = f"INSERT INTO {current_app.config['COUNT']['table_name']} DEFAULT VALUES returning id;"
    # We launch the query
    count, success = fetchall_db(sql_request)
    return success


def too_many_count():
    """
    Function to return the issue from our API when we have too many count from today
    """
    return jsonify({"error" :f"Too many connections for today, limited to " \
           f"{current_app.config['COUNT']['count_total_per_day']} per day"}), 401
