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

#------------------------------------------------------------------
# Funktion som omvandlar måltavlan till en sträng
def targets_to_string(targets):
    result = ""
    for target in targets:
        if is_closed(target):  # Om målet är stängt
            result += "* "
        else:  # Om målet är öppet
            result += "0 "
    return result  # Returnerar den formaterade strängen

# Funktion som visar måltavlan på skärmen
def view_targets(targets):
    # Rad med numrering (index)
    print("  " + " ".join([str(i) for i in range(len(targets))]))
    
    # Rad med mål (öppna eller stängda)
    print("  " + targets_to_string(targets))

# Testa funktionerna
ts = new_targets()
view_targets(ts)  # Visar en måltavla med alla öppna mål

close_target(ts, 3)  # Stänger mål på position 3
view_targets(ts)  # Visar uppdaterad måltavla med ett stängt mål

close_target(ts, 0)  # Stänger mål på position 0
view_targets(ts)  # Visar uppdaterad måltavla med två stängda mål

#------------------------------------------------------------------
from random import randint

# Funktion som simulerar en träff eller miss med 50 % sannolikhet
def random_hit():
    return randint(0, 1) == 1  # Returnerar True om det slumpade värdet är 1, annars False

# Funktion som skjuter på en specifik måltavla och position
def shoot(targets, position):
    if is_open(targets[position]):
        if random_hit():  # Om det är en träff
            close_target(targets, position)  # Stänger målet
            return "Hit on open target"
        else:
            return "Miss"
    elif is_closed(targets[position]):
        return "Hit on closed target"

# Testa funktionerna
ts = new_targets()
view_targets(ts)

# Försök skjuta på olika mål och observera resultaten
print(shoot(ts, 0))  # Försöker skjuta på mål 0
view_targets(ts)

print(shoot(ts, 0))  # Försöker skjuta på mål 0 igen
view_targets(ts)

print(shoot(ts, 4))  # Försöker skjuta på mål 4
view_targets(ts)


