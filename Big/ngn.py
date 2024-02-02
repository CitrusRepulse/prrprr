chart = {
    'A': 'B', 
    'B': 'C', 
    'C': 'D', 
    'D': 'E', 
    'E': 'F', 
    'F': 'G',
    'G': 'H', 
    'H': 'I', 
    'I': 'J', 
    'J': 'K', 
    'K': 'L', 
    'L': 'M',
    'M': 'N', 
    'N': 'O', 
    'O': 'P', 
    'P': 'Q', 
    'Q': 'R', 
    'R': 'S',
    'S': 'T', 
    'T': 'U', 
    'U': 'V', 
    'V': 'W', 
    'W': 'X', 
    'X': 'Y',
    'Y': 'Z', 
    'Z': 'Å',
    'Å': 'Ä', 
    'Ä': 'Ö', 
    'Ö': 'A',
    ' ': ' ',
    '0': '9', 
    '1': '0',
    '2': '1', 
    '3': '2', 
    '4': '3', 
    '5': '4',
    '6': '5', 
    '7': '6', 
    '8': '7', 
    '9': '8',
}
while True:
    text = input("Mata in text: ").upper()
    svaret = ""

    for i in range(len(text)):
        key = text[i]
        svar = chart.get(key)
        svaret += svar + ""

    print(svaret)