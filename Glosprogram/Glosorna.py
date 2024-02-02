import os
import sqlite3 as sql

def connect():
    sqLista = sql.connect("glos.db")
    cursor = sqLista.cursor()
    return sqLista, cursor

def addList(nativ, trans, sqLista, cursor):
    cursor.execute(f"""INSERT INTO Gloslista (na, tr)
                   VALUES ("{nativ}","{trans}")""")
    sqLista.commit()

def showList(cursor):
    words = []
    
    cursor.execute("""SELECT * FROM Glosor""")
    for obj in cursor:
        words.append(obj)

        return words
    
def delete(sqList, cursor):
    cursor.execute("""DELETE FROM Gloslista""")
    sqList.commit()