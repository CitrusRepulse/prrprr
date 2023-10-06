import bil


looping = True

volvo_svart = bil.Bil("Volvo", "grön", 3)
fiat_bit = bil.Bil("fiat", "röd", 12)
bugatti_rosa = bil.Bil("bugatti", "svart & blå", 3)
mazda_gul = bil.Bil("mazda", "gul", 5)

billista = [volvo_svart, fiat_bit, bugatti_rosa, mazda_gul]


#print(f"första bilen i listan = {billista[3].fabrikat}")

while looping:
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("\n\t -=:BilAutomat:=-")

    i=0
    
    for bil in billista:
        print(f"{i+1} : {bil.fabrikat} : {bil.color} : Antal={bil.lager}")
        i = i + 1

    bil_nr = input("\nMata in siffra för vald bil: ")

    bil_nr_int = int(bil_nr)

    lager_int = billista[bil_nr_int-1].getLager()
    lager_string = str(bil_nr)

    if lager_int > 0:
        print(f"\nEn {billista[bil_nr_int-1].color} {billista[bil_nr_int-1].fabrikat} kom här")


        nytt_lagersaldo_int = lager_int - 1
        nytt_lagersaldo_str = int(nytt_lagersaldo_int)

        billista[bil_nr_int-1].setLager(nytt_lagersaldo_int)

    else :
        print(f"Tyvärr slut på biltyper{billista[bil_nr_int-1].fabrikat}")


    print(f"Lager saldo före: {lager_string} st")
    print(f"Lager saldo efter: {nytt_lagersaldo_str}")
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")

    go = input("Vill du avsluta programmet? j/n")

    if (go == "j"):
        break