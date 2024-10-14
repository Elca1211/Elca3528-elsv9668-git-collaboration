
def menu(title, prompt, options):
    print(f"\n{title}\n") # skriver ut titeln för menyn
    
    # Skriver ut varje alternativ i ordlistan options
    for option, description in options.items():
        print(f"  {option}) {description}")
    
    # Fortsätter att fråga användaren tills ett giltigt alternativ matas in
    while True:
        choice = input(f"\n{prompt}").lower()  # Konverterar input till gemener
        if choice in options:
            return choice  # Returnerar det giltiga valet

def login(users):
    # skriver först ut inputsen 
    while True:
        username = input("\n     User: ")
        password = input("\n Password: ")
        
        # Kontollerar inmatningen
        if username in users and users[username] == password:
            return username # om användarnamnet med tillhörande lösenord finns med i ordlistan retuneras användarnamnet 
        
        else:
            print("Invalid username or password")
            options2 = {"r": "Try again", "q": "Quit"}
            choice = menu("What do you want to do?", "My choice: ", options2)
            
            if choice == "q":
                return None
            
# Testfall
users = {"nisse":"apa", "stina":"t-rex", "bosse":"ko"}
user = login(users)



