import pandas as pd
import pyfiglet
from art import text2art

# Funktion för rubrik i ASCII-stil
def visa_ascii_rubrik(text, font="slant", färg="\033[94m"):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print(f"{färg}{ascii_art}\033[0m")

# Funktion för att visa menyn med tydligare formatering
def show_menu():
    visa_ascii_rubrik("Glosmaskinen", "slant")
    print("\033[94m            Här kan du bli expert på dina glosor!\n\n\033[0m")
    print("Välj ett alternativ:")
    print("──────────────────────────────")
    for option, description in options.items():
        print(f"   {option}) {description}")
    print("──────────────────────────────")

# Funktion för att färga text
def färgad_text(text, färg="grön"):
    färger = {
        "grön": "\033[92m",
        "röd": "\033[91m",
        "blå": "\033[94m",
        "orange": "\033[93m",
        "slut": "\033[0m"
    }
    return färger.get(färg, "") + text + färger["slut"]

# Ladda CSV-filen
filnamn = '/Users/elsasvardstrom/Downloads/glosor.csv'
df = pd.read_csv(filnamn, sep=';')

# Menyalternativ
options = {
    "a": "Skriva in egna glosor",
    "b": "Öva på färdiga glosor",
    "q": "Avsluta Glosmaskinen :("
}

def egna_glosor():
    antal = int(input("\nHur många glosor vill du skriva in? "))
    sprak1 = []
    sprak2 = []
    sprak1namn = input("Vad heter språk 1? ")
    sprak2namn = input("Vad heter språk 2? ")

    for i in range(antal):
        glosa1 = input(f"\nAnge glosa {i + 1} för {sprak1namn}: ")
        sprak1.append(glosa1)
        glosa2 = input(f"Ange glosa {i + 1} för {sprak2namn}: ")
        sprak2.append(glosa2)

    poäng = 0
    for i in range(len(sprak1)):
        print(f"\nÖversätt '{sprak1[i]}' till {sprak2namn}:")
        gissn = input("Ditt svar: ")
        if gissn.lower() == sprak2[i].lower():
            print(färgad_text(f"\nRätt! {sprak1[i]} = {sprak2[i]}", "grön"))
            poäng += 1
        else:
            print(färgad_text(f"\nFel! Det ska vara: {sprak2[i]}", "röd"))
    
    print(färgad_text(f"\nDu hade {poäng} rätt av {antal}, bra jobbat!", "blå"))
    print(f"------------------------------------------------------------------------\n")

def öva_glosor(nivå, språk):
    if nivå == 1:
        glosor_nivå = df.iloc[:10]
    elif nivå == 2:
        glosor_nivå = df.iloc[10:20]
    elif nivå == 3:
        glosor_nivå = df.iloc[20:30]
    else:
        print(färgad_text("Ogiltig nivå, skriv 1, 2 eller 3.\n", "orange"))
        return

    poäng = 0
    for _, row in glosor_nivå.iterrows():
        svenska = row['Svenska']
        korrekt = row[språk.capitalize()]

        # Visa glosan som vanlig text istället för ASCII
        print(f"\nÖversätt '{svenska}' till {språk}:")
        gissn = input("Ditt svar: ")
        
        if gissn.lower() == korrekt.lower():
            print(färgad_text(f"Rätt! {svenska} = {korrekt}", "grön"))
            poäng += 1
        else:
            print(färgad_text(f"Fel! Det ska vara: {korrekt}.", "röd"))

    print(färgad_text(f"\nDu hade {poäng} av 10 rätt på nivå {nivå}.", "blå")) # blå 
    print(f"------------------------------------------------------------------------\n")


# Huvudprogram
while True:
    show_menu()
    choice = input("\nDitt val: ").lower()
    if choice in options:
        print(f"\nDu valde: {choice}) {options[choice]}")
        if choice == "a":
            egna_glosor()
        elif choice == "b":
            try:
                nivå = int(input("Vilken nivå vill du öva på? (1, 2 eller 3): "))
                språk = input("Vilket språk vill du öva på? (engelska, spanska eller tyska): ").lower()
                if språk in ["engelska", "spanska", "tyska"]:
                    öva_glosor(nivå, språk)
                else:
                    print(färgad_text("Ogiltigt språk.", "orange"))  
            except ValueError:
                print(färgad_text("Vänligen ange ett heltal för nivån.", "orange")) # orange 
        elif choice == "q":
            print(färgad_text("Avslutar Glosmaskinen.", "röd"))
            break
    else:
        print(färgad_text("Felaktigt val, försök igen.", "orange"))
