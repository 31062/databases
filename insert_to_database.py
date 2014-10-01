import sqlite3
# open exsisting database or create a new one
with sqlite3.connect("shop.db") as db:
    #make cursor
    cursor = db.cursor()
    new_coffie = ("latte",45.46)
    sql = """insert into Product(Name,Price)
    values (?,?)"""
    cursor.execute(sql)
    db.commit()
