options = {"a":"Add item", "l":"List items", "q":"Log out"}

# funktion för att visa menyn
def show_menu():
    print("\nSelect an action:\n")
    for option, description in options.items():
        print(f"   {option}) {description}")
        
# Fortsätter fråga om alternativ tills ett giltigt svar matas in
while True:
    show_menu()
    choice = input("\nOption: ").lower() # konventerar input till gemener för att hantera stora/små bokstäver
    if choice in options:
        print(f"\nYou selected option {choice}) {options[choice]}")
        break
