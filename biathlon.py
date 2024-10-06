def splash():
    print("\n" + "~" * 38)
    print(" " * 14 + "Biathlon\n")
    print(" " * 9 + "a hit or miss game")
    print("~" * 38 + "\n")
    
# Globala variabler
open = 0
closed = 1
targets = [1, 2, 3, 4, 5]

def is_open(value):
    # Jämför 'value' med det globala värdet 'open'
    return value == open  # Returnera True om 'value' är lika med 'open', annars False

# Exempel på användning:
print(is_open(0))  # printar då True
print(is_open(1))  # printar då False


def is_closed(value):
    # Jämför 'value' med det globala värdet 'closed'
    return value == closed  # Returnera True om 'value' är lika med 'closed', annars False

# Exempel på användning:
print(is_closed(0))  # printar då False
print(is_closed(1))  # printar då True 


def new_targets():
    # Skapa och returnera en lista med fem öppna mål, där varje mål är lika med 'open'
    return [open] * 5  # Skapar en lista med 5 element som alla är värdet av 'open'

# Exempel på användning
print(new_targets())  # Förväntat [0, 0, 0, 0, 0] om 'open' är 0

