# Definerar funktionen menu()
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

# Testfall 1
options1 = {"a": "Add item", "l": "List items", "q": "Log out"}
opt1 = menu("Select an action", "Action: ", options1)
print(f"\nYou selected action {opt1}) {options1[opt1]}")
print()

# Testfall 2
options2 = {"r": "Try again", "q": "Quit"}
opt2 = menu("What do you want to do?", "My choice: ", options2)
print(f"\nYou selected option {opt2}) {options2[opt2]}")

    
