import sqlite3
database ="database/employees.sqlite3"

def get_connection():
    try:
        conn = sqlite3.connect(database)
        return conn
    except Exception as e:
        print(e)