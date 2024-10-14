# Definerar funktionen
def login(users):
    # skriver först ut inputsen 
    while True:
        username = input("\n     User: ")
        password = input("\n Password: ")
        
        # Kontollerar inmatningen
        if username in users and users[username] == password:
            return username # om användarnamnet med tillhörande lösenord finns med i ordlistan retuneras användarnamnet 
        
        else: # om inte (användarnamnet eller lösenordet fel) skrivs strängen nedan ut
            print("Invalid username or password")
    

# Test 1 
users1 = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"} # skapar en test ordlista
user1 = login(users1) # anropar funktionen till ordlistan users1
print(f"Welcome {user1}") # skriver ut welcome {username} (returvärdet) när loopen avslutas, dvs när inmataren har matat in korrekt användarnamn OCH lösenord

# Test 2
users2 = {"foo":"123", "bar":"hello", "foobar":"hello123"}
user2 = login(users2)
print(f"Welcome {user2}")