# Ordlista med tillhörande lösenord 
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}

# En loop som körs tills användaren matar in ett korrekt användarnamn och lösenord
while True:
    # Läser in inmatarens användarnamn och lösenord
    username = input("\n     User: ")
    password = input("\n Password: ")
    
    # Kontollerar om användarnamnet OCH lösenordet finns i ordlistan 
    if username in users and users[username] == password: # "if username in users" kollar om inmatarens användarnamn finns i ordlistan
        # "and users[username] == password" kollar om inmatarens lösenord också är korrekt, dvs att användarnamnets tillhörande lösen är korrekt
        # Loopen kontrollerar att båda inmatningarna är korrekt 
        print(f"\nWelcome {username}")
        break # Om det är korrekt avslutas loopen 
    
    else: # Om antingen lösenordet, användaren är fel skrivs meddelandet nedan ut och inmataren får testa inlogget tills den får rätt svar 
        print(f"Invalid username or password")

# >>> users["nisse"]
# 'apa'
# >>> users["stina"]
# 't-rex'
# >>> users["bosse"]
# 'ko'