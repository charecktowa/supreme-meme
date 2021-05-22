import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    connection = None

    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return connection

def create_tables(conn):
    table = """
        CREATE TABLE devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_ip TEXT NOT NULL,
            campus TEXT NOT NULL,
            division TEXT NOT NULL,
            device_location TEXT NOT NULL
        );
            """
    try:
        c = conn.cursor()
        c.execute(table)
    except Error as e:
        print(e)

if __name__ == '__main__':
    conn = create_connection('test.db')

    if conn is not None:
        create_tables(conn)
    else:
        print('Algo pasó. Ups.')