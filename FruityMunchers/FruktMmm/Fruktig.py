#Visar vad funktioner är, vad de har för nytta, främst för att inte repetera kod och samla kod blocken
#Går även igenom arrayer.

import random

#Skapar en Tuple
frukter = ("Banan", "Melon", "Kiwi", "Citron")
looping = True

#Definerar python funktioner
def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + frukter[fnr-1] + " kommer här\n")


while looping:
    print("________________________________________________________________")
    


    i=0

    for frukt in frukter:
        print(f"{str(i+1)} : {frukt}")
        i += 1


    fruktnr = input("\n Mata in nummer på frukt du vill ha: ")

    print_fruit(fruktnr)

    go = input("Vill du välja en frukt till j/n : j")
    print("\n")

    if go == "n":
        break