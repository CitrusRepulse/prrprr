personnummer = input("Mata in ditt personnummer: ")

total = 0
perNr = []

for numbers in personnummer:
    perNr.append(int(numbers))

for i in range(len(personnummer)):
    
    if i % 2 == 0:

        int(personnummer[i]) * 2
        
        if perNr[i] >= 10:
            nr1 = perNr[i][:1]
            nr2 = perNr[i][-1:]
            total += nr1 + nr2
        else:
            total += perNr[i] 


checkNr = (10-(total % 10))%10
    
if checkNr == perNr[9]:
    print("Ditt personnummer stämmer")
else:
    print("Fel personnummer.")