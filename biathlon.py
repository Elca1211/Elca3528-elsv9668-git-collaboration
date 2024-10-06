def splash():
    print("\n" + "~" * 38)
    print(" " * 14 + "Biathlon\n")
    print(" " * 9 + "a hit or miss game")
    print("~" * 38 + "\n")
    
# Globala variabler
open = 0
closed = 1

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


def close_target(targets, position):
    targets[position] = closed
    return targets

# test exempel
ts = new_targets()
print(ts)
ts = close_target(ts, 3)
print(ts)
ts = close_target(ts, 4)
print(ts)

#---------------------------------------------------------------

# Funktion för att räkna stängda mål
def points(targets):
    # Variabel för att hålla räkningen av stängda mål
    n = 0
    # Loopa genom varje mål i targets
    for target in targets:
        # Kontrollera om målet är stängt
        if is_closed(target):
            # Om det är stängt, öka räknaren
            n += 1
    # Returnera antalet stängda mål
    return n

# Testa funktionen
ts = new_targets()  # Skapar en ny måltavla [0, 0, 0, 0, 0]
print(points(ts))  # Förväntat resultat: 0

close_target(ts, 2)  # Stänger mål på position 2
print(points(ts))  # Förväntat resultat: 1

close_target(ts, 0)  # Stänger mål på position 0
close_target(ts, 4)  # Stänger mål på position 4
print(points(ts))  # Förväntat resultat: 3

close_target(ts, 3)  # Stänger mål på position 3
close_target(ts, 1)  # Stänger mål på position 1
print(points(ts))  # Förväntat resultat: 5

