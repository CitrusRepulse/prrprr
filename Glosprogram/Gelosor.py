import os
import sqlite3 as sql
import Glosorna
import random

sqLista, cursor = Glosorna.connect()

frst = input("vill du börja med nya glosor? j/n")

if frst == 'j':
    Glosorna.delete(sqLista,cursor)

mode = input("Hur vill du ha dina glosor? 1 för svenska till eneglska eller 2 för engelska till svenska:")

if mode == 1:
    nativ = "svenska"
    trans = "engelska"
else:
    nativ = "engelska"
    trans = "svenska"

cont = 'j'

while cont == 'j':

    svenska = input("Mata in ord på svenska:")
    trans = input("Mata in översatta ordet:")

    Glosorna.addList(nativ, trans, sqLista, cursor)

    resp = input("Mata in j om du vill fortsätta, annars n: ")

show = Glosorna.showList(cursor)

while len(show) != 0:
    word = random.choice(show)
    svar = input(f"Översätt {word[1]} till {trans}: ")
    if svar == word[2]:
        print("Bra jobbat!")
    else:
        print ("Nu blev det fel...")

    show.remove(word)

print("Du är klar. :)")