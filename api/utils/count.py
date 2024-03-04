from database import fetchall_db


TABLE_COUNT = "count_per_day"

def get_count_per_day():
    """
    Function to get the current count of connection for today
    """
    # We create the query
    sql_request = f"SELECT count FROM {TABLE_COUNT} WHERE date is CURRENT_DATE"
    # We launch the connection to our database
    count = fetchall_db(sql_request, req_type="SELECT")

    # We return the count
    return count


def check_count_per_day():
    """
    Function to check if we already have too many connections for today on our api
    """

    # We get back the count of connection for today
    count = get_count_per_day()

    # If no connection
    if not count:
        # We create the row in database and we return True
        create_count()
        return True

    # If less than 50 connections
    elif count < 50:
        # We update the count and we return True
        update_count()
        return True

    # More than 50 connections
    else:
        # We return False
        return False


def update_count():
    """
    We update the count of connection for today with a +1
    :return:
    """
    sql_request = f"UPDATE {TABLE_COUNT} SET total = total + 1 WHERE date = CURRENT_DATE RETURNING *;"
    count = fetchall_db(sql_request, req_type="UPDATE")


def create_count():
    """
        We create the first connection of the day
        :return:
        """
    sql_request = f"INSERT INTO {TABLE_COUNT} DEFAULT VALUES returning id;"
    count = fetchall_db(sql_request, req_type="INSERT")



