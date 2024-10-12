# Definerar funktionen add

def add(prompt, strings): 
    new_duck = input(prompt) 
    strings.append(new_duck) 
    return strings 

# Testar funktionen med olika värden på argumenten
ducks = ["Huey", "Dewey", "Louie"]

print(f"         Ducks: {ducks}\n")


add("    Add a duck: ", ducks)
print(f"\n         Ducks: {ducks}\n")


composers = ["Mozart", "Bach"]
print(f"     Composers: {composers}\n")


add("Add a composer: ", composers)
print(f"\n     Composers: {composers}\n")
