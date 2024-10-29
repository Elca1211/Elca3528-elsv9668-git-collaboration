import pandas as pd

filnamn = '/Users/elsasvardstrom/Downloads/glosor.csv'  # Byt ut 'din_fil.csv' mot namnet på din fil

# Läs in CSV-filen
df = pd.read_csv(filnamn, sep=';')

options = {
    "a": "Skriva in egna glosor",
    "b": "Öva på färdiga glosor",
    "q": "Avsluta Glosmaskinen :("
}

# Funktion för att visa menyn
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
    poäng = 0

    for i in range(antal):
        nummer += 1
        glosaspr1 = input("Ange glosa " + str(nummer) +  " för " + sprak1namn + ": ")
        sprak1.append(glosaspr1)
        glosaspr2 = input("Ange glosa " + str(nummer) + " för " + sprak2namn + ": ")
        sprak2.append(glosaspr2)

    for i in range(len(sprak1)):
        gissn = input("Skriv " + sprak1[i] + " på " + sprak2namn + ": ")
        if gissn.lower() == sprak2[i].lower():
            print("Rätt! " + sprak1[i] + "=" + sprak2[i])
            poäng += 1
        else:
            print("Fel!")
            print("Det ska vara: " + sprak2[i] + ".")
    
    print("Du hade " + str(poäng) + " rätt, bra jobbat!")

def öva_glosor(nivå, språk):
    if nivå == 1:
        glosor_nivå = df.iloc[:10]
    elif nivå == 2:
        glosor_nivå = df.iloc[10:20]
    elif nivå == 3:
        glosor_nivå = df.iloc[20:30]
    else:
        print("Ogiltig nivå, skriv 1, 2, eller 3.")
        return

    poäng = 0

    for index, row in glosor_nivå.iterrows():
        svenska = row['Svenska']  # Använd kolumnnamnet för svenska
        # Välj korrekt kolumn baserat på språk
        if språk == "engelska":
            korrekt = row['Engelska']
        elif språk == "spanska":
            korrekt = row['Spanska']
        elif språk == "tyska":
            korrekt = row['Tyska']
        else:
            print("Ogiltigt språk.")
            return

        # Fråga användaren
        gissn = input(f"Skriv '{svenska}' på {språk}: ")

        if gissn.lower() == korrekt.lower():
            print(f"Rätt! {svenska} = {korrekt}")
            poäng += 1
        else:
            print(f"Fel! Det ska vara: {korrekt}.")

    print(f"Du hade {poäng} av 10 rätt på nivå {nivå}.")

# Huvudprogram för att välja nivå och språk
while True:
    show_menu()
    choice = input("\nDitt val: ").lower()
    if choice in options:
        print(f"\nDu valde: {choice}) {options[choice]}")
        if choice == "a":
            egna_glosor()
        
        if choice == "b":
            try:
                nivå = int(input("Vilken nivå vill du öva på? (1, 2 eller 3): "))
                
                while True:
                    språk = input("Vilket språk vill du öva på? (engelska, spanska eller tyska): ").lower()

                    if språk in ["engelska", "spanska", "tyska"]:
                        öva_glosor(nivå, språk)
                        break  # Bryt ut ur språkloopen om ett giltigt språk anges
                    else:
                        print("Ogiltigt språk, vänligen välj mellan engelska, spanska eller tyska.")
                
            except ValueError:
                print("Vänligen ange ett heltal för nivån.")

        elif choice == "q":
            print("Avslutar Glosmaskinen.")
            break
    else:
        print("Felaktigt val, försök igen.")
