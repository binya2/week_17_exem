import mysql.connector
from mysql.connector import Error

from congif import mysql_config


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=mysql_config.MYSQL_HOST,
            user=mysql_config.MYSQL_USER,
            password=mysql_config.MYSQL_ROOT_PASSWORD,
            database="dev_db"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        raise