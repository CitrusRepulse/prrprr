
text = input("Vad vill du ha översatt till skottskrik: ").lower()
skott = ""
for v in text:
    if v == "a" or v == "o" or v == "i" or v == "y" or v == "å" or v == "ä" or v == "ö":
        v = "e"
    
    skott += v
    
print(skott.upper())