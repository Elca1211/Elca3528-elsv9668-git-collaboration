# funktionen add

def add(prompt, strings): 
    new_duck = input(prompt) 
    strings.append(new_duck) 
    return strings

# funktionen view
def view(description, strings):
    print(description)
    n = 1
    for string in strings:
        print(f" {n}) {string}\n") 
        n += 1
    return None

# skapar en tom lista 
strings = []

# Initierar varibeln n till 4
n = 4

print(f"n = {n}\n") # Skriver ut värdet på n 

for _ in range(n): # For loop där användaren n ggr matar in strängar till listan string
    add("Lägg till en sträng: ", strings)

# skapar beskrivningen/rubriken för resultatet 
description = f"\nDu har matat in följande {n} strängar\n"

view(description, strings) # anropar funktionen view med beskrvningen och den skapade listan string
