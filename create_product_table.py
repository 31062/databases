import sqlite3

def create_table(db_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor
