import sqlite3
def create_database():
    #creates a data base
    with sqlite3.connect("coffie_shop.db") as db:
        #make cursor
        cursor = db.cursor()
        sql = ("""create table Product(ProductID interger
              Name text
              Price real,
              Primary Key(ProductID))""")
        db.commit()

def insert_to_database():
    
    
