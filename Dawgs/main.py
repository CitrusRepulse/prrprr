import os
import sqlite3
from sqlite3 import Error

#main
def main():

    add_dog_to_table()
    list_dog_table()

def list_dog_table():
    #DB con
    sqliteConnection = sqlite3.connect("dogs.db")
    cursor = sqliteConnection.cursor()

    sqlite_insert_query ="""SELECT * from dogs ORDER By name """
    cursor.execute(sqlite_insert_query)
    records = cursor.fetchall()



    for row in records:
        print(f"\tID: {row[0]}, \tNAMN: {row[1]}, \RAS: {row[2]}")


        cursor.close
        #Close cursor & connection
        sqliteConnection.close()


def add_dog_to_table():
    os.system('cls' if os.name == 'nt' else 'clear')
    hundnamn = input("Mata in hund namn: ")
    hundras = input("Mata in hund ras: ")

    sqliteConnection = sqlite3.connect("dogs.db")
    cursor = sqliteConnection.cursor()
    sqlite_insert_query = f"""INSERT INTO dogs
                        (name, ras)
                        VALUES
                        ('{hundnamn}', '{hundras}')"""
    
    cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Closed")
    #Off
    cursor.close()
        #Off connection
    sqliteConnection.close()
    
main()