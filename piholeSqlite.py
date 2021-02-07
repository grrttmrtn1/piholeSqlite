import sqlite3
from sqlite3 import Error

class piholeSqlite:

    def __init__(self, db_file, query):
        self.db_file = db_file
        self.query = query

    def create_connection (self):
        try:
            conn = sqlite3.connect (self.db_file)
            return conn
        except Error as e:
            print(e)
        return None

    def runQuery (self, conn):
        conn.text_factory = str
        cur = conn.cursor()
        cur.execute (self.query)
        rows = cur.fetchall()
        return rows
