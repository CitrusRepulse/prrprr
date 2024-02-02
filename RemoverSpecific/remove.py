txt = open('konvo.txt', 'r', encoding='utf-8-sig')
data = txt.readlines()

tabort = input("Vem ska tas bort? ")

for i in range(len(data)):
    txt = data[i].rstrip(':')

    if txt == tabort:
        data.pop(txt)

print(data)