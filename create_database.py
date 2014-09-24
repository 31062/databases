import sqlite3
# open exsisting database or create a new one
with sqlite3.connect("shop.db") as db:
    #make cursor
    cursor = db.cursor()
    cursor.execute(""" create table Product(ProductID interger,
    Name text,
    Price real,
    Primary key(ProductID))""")
    db.commit()
