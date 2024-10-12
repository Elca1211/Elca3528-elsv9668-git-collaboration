# Programmet skall:
# 1. skriva ut listan med ankor
# 2. fråga användaren efter namnet på en anka
# 3. lägga till den nya ankan sist i listan ducks
# 4. skriva ut den uppdaterade listan med ankor.

ducks = ["Huey", "Dewey", "Louie"] # Skapar listan ducks
print(f"List of ducks: {ducks}\n")

# Definerar funktionen add
def add(prompt, strings): # Prompt och strings är här abstrakta parametrar
    new_duck = input(prompt) # Användaren skriver till en ny anka 
    strings.append(new_duck) # Nya ankan läggs till längst bak i listan
    return strings # Den uppdaterade listan retuneras

# Anropar funktionen med värden för prompt och strings
updated_ducks = add("Add a duck: ", ducks)

# Skriver ut den uppdaterade listan med ankor
print(f"\nUpdated list of ducks: {updated_ducks}\n")
