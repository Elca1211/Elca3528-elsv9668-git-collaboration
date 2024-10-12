# Listor (globala) 
names   = ["nisse", "stina", "bosse", "mimmi"]
animals = ["giraff", "myrslok", "tapir"]

# Definerar funktionen view
def view(description, strings):
#----------------------------------------------
#Skriver ut en beskrivning och numrerad lista av strängar. 

# Argument:
# description = en sträng som beskriver vad listorna innehåller
# strings = en lista med strängar som ska skrivas ut

# Retunerar None 
    
#----------------------------------------------
    print(description) # Skriver ut beskrivning 
    num = 1 # lokal varibel, antar startvärdet 1
    for string in strings: # loopar igenom varje sträng/ element i listan 
        print(f" {num}) {string}\n") # skriver ut radnummer och sträng
        num += 1 # ökar radnumret med 1 för varje iteration
    return None

# Testar funktionerna

view("Lista med namn: \n", names) # anropar view med listan names med beskrivningen

view("\nLista med djur: \n", animals) # anropar  view listan animals med beskrivningen
