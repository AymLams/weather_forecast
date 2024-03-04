import psycopg2
from flask import current_app


def fetchall_db(request: str, req_type: str):
    """
    Function to launch a query to our sql
    :param request:
    :return:
    """
    try:
        con = psycopg2.connect(
            database=current_app.config["sql"],
            user=current_app.config["user"],
            password=current_app.config["password"],
            port=current_app.config["port"]
        )
        cursor = con.cursor()
        cursor.execute(request)

        if req_type == "SELECT":
            result = cursor.fetchall()
            cursor.close()
            return result

        elif req_type in ("DELETE", "UPDATE", "INSERT"):
            con.commit()
            cursor.close()
    except:
        # GESTION DE L EXCEPT A FAIRE
