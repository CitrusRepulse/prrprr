import random

valörer = ["Spader", "Hjärter", "Ruter", "Klöver"]
värden = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'knäckt', 'Dam', 'Kung', 'Ess']

lek = []

for valör in valörer:
    for värde in värden:
        lek.append (f'{valör} {värde}')

random.shuffle(lek)

def dela_kort (hand: list, lek: list):
    kort = lek[0]
    lek.pop(0)
    hand.append(kort)

def räkna_hand_värde(hand):
    value = 0
    has_ace = False

    for kort in hand:
        värde = kort.split()[0]

        if värde.nummer():
            value += int(värde)
        elif värde in ['Dam', 'Knäckt', 'Kung']:
            value += 10
        elif värde == 'Ess':
            has_ace = True
            value += 11
    if has_ace and value > 21:
        value -= 10
    
    return value


spelare_hand = []
dealer_hand = []

dela_kort(lek, spelare_hand)
dela_kort(lek, spelare_hand)
dela_kort(lek, dealer_hand)
dela_kort(lek, dealer_hand)

while True:
    print(f'spelarens hand: {spelare_hand} ({räkna_hand_värde(spelare_hand)})')
    print(f'dealerns hand: [{dealer_hand [0]} |||||||]')

    if räkna_hand_värde(spelare_hand) > 21:
        print('Du förlorade :(')

    action = input("Vill du fortsätta eller stå över?")
