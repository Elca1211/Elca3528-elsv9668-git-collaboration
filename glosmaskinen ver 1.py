options = {"a":"Skriva in egna glosor", "b":"Öva på färdiga glosor", "q":"Avsluta Glosmaskinen :("}

# funktion för att visa menyn
def show_menu():
    print("Välkommen till Glosmaskinen!\nHär kan du bli expert på dina glosor!")
    print("\nVad vill du göra?:\n")
    for option, description in options.items():
        print(f"   {option}) {description}")

def egna_glosor():
    antal = int(input("Hur många glosor vill du skriva in? "))
    sprak1 = []
    sprak2 = []
    sprak1namn = input("Vad heter språk 1? ")
    sprak2namn = input("Vad heter språk 2? ")
    
    nummer = 0
    nummer2 = 0
    poäng = 0

    for i in range(antal):
        nummer += 1
        glosaspr1 = input("Ange glosa " + str(nummer) +  " för " + sprak1namn + ": ")
        sprak1.append(glosaspr1)
        glosaspr2 = input("Ange glosa " + str(nummer) + " för " + sprak2namn + ": ")
        sprak2.append(glosaspr2)

    for i in range(len(sprak1)):
        gissn = input("Skriv " + sprak1[i] + " på " + sprak2namn + ": ")
        if gissn == sprak2[i]:
            print("Rätt! " + sprak1[i] + "=" + sprak2[i])
            poäng += 1
        else:
            print("Fel!")
            print("Det ska vara: " + sprak2[i] + ".")
    
    print("Du hade " + str(poäng) + " rätt, bra jobbat!")

while True:
    show_menu()
    choice = input("\nDitt val: ").lower()
    if choice in options:
        print(f"\nDu valde: {choice}) {options[choice]}")
        if choice == "a":
            egna_glosor()
        
        elif choice == "q":
            print("Avslutar Glosmaskinen.")
            break
    else:
        print("Felaktigt val, försök igen.")
