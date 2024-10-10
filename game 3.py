
# BIATHLON A HIT OR MISS GAME 

#-----------------------------------------------------------------------------------
# Funktioner
#-----------------------------------------------------------------------------------

# Importera nödvändiga moduler och funktioner

from random import randint  # Importerar funktionen randint från python-modulen random för att generera slumpmässiga heltal (används senare i "random_hit()")


# Skriver ut spelets titel och introduktion
def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon")
    print()
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # Inget returvärde, ingen sidoeffekt annat än att visa information för spelaren.


# Skapar en ny måltavla representerad som en lista med fem öppna mål ([0, 0, 0, 0, 0]). (Öppet mål = 0) 
def new_targets():
    return [0, 0, 0, 0, 0] # Returnerar en listan till spelaren. 


# Kontroll av öppet mål
def is_open(target): # (0) - målet är öppet 
    return target == 0


# Kontroll om målset är stängt
def is_closed(target): # (1) - målet är stängt 
    return target == 1


# Träff, stänger mål vid träff 
def close_target(targets, position): # ändrar värdet från 0 till 1) vid angiven position om det är öppet.
    if is_open(targets[position]):
        targets[position] = 1 # om det är öppet ändras måltavlan vid den positionen till 1, dvs målet är stängt


# Slumpen, träffsäkerheten = 50%
def random_hit():
    return randint(0, 1) == 1 # Blir random 1 eller 0, dvs ca 50% chans att det blir en etta när man siktar mot ett mål
# Returnerar True med 50% sannolikhet (träff) och False med 50% sannolikhet (miss)


# Hanterar skott mot ett specifikt mål baserat på en slumphändelse, retuneras strängar 
def shoot(targets, position): 
    if is_closed(targets[position]): # Om man träffar ett stängt mål 
        return "Hit on closed target"
    elif random_hit(): # 50 % chans för träff om man skjuter mot ett öppet mål (random_hit() = True)
        close_target(targets, position) # Om man träffar ett öppet mål
        return "Hit on open target" 
    else:
        return "Miss" # Om man siktar mot ett öppet mål, men missar pågrund av slumpen, retuneras strängen "Miss" (random_hit() = False)


# Skriver ut resultat måltavlan
def targets_to_string(targets): # targets = listan med nollor och ettor 
    result = "" # Resultas måltavlan är först tom 
    for target in targets:
        if is_closed(target):  # Om målet är stängt --> dvs en träff
            result += "* " # öka antalet * med 1 på måltavlan 
        else:  # Om målet är öppet (dvs en miss)
            result += "O " # antalet missar, Antalet öppna mål kvar 
    return result  # Returnerar den formaterade strängen


# Visar måltavlan och dess numreringar 
def view_targets(targets): 
    print("\n  1 2 3 4 5\n") # Skriver ut listan med de numrerade positionerna (\n = blank rad) 
    print("  " + targets_to_string(targets) + "\n") # Skriver ut måltavlan 



# Poängräknare 
def points(targets):
    # Variabel för att hålla räkningen av stängda mål
    n = 0
    # Loopa genom varje mål i targets
    for target in targets:
        # Kontrollera om målet är stängt
        if is_closed(target):
            # Om det är stängt, öka räknaren
            n += 1
    # Returnera antalet stängda mål
    return n



# Omvandlar de verkliga indexen (0-4) till (1-5) från spelarens input
def parse_target(string): # Kontrollera om strängen kan konverteras till ett heltal (är numerisk)
    
    # Konverterar strängen till ett heltal
    if string.isnumeric():
       
       # Om talet är mellan 1 och 5, returnera motsvarande index (0-4)
        num = int(string) 
        
        if 1 <= num <= 5: # talen 1-5
            return num - 1 # Omvandlingen från verkliga index, ex om man skriver 1: 1-1=0 som är index [0]
   
   # Om det inte är en giltig sträng, returnera None
    return None


#-----------------------------------------------------------------------------------
# Huvudspel
#-----------------------------------------------------------------------------------
def play_game():
    splash()  # Visa spelets titel och introduktion
    shots = 5  # Antal skott
    current_shot = 0  # Skott räknare, start 0 = skott använda
    targets = new_targets()  # Skapa ny måltavla
    view_targets(targets)  # Visa måltavlan

    while current_shot < shots: # går från 1 - 5 (5 skott)
        current_shot += 1
        position = parse_target(input(f"Shot nr {current_shot} at: ")) # stäng retuneras 
        if position is None:
            print("Please enter a valid position between 1 and 5.") # fel index inmatning
            continue 
        
        result = shoot(targets, position)
        print(result)
        view_targets(targets)

    # När alla skott är slut, visa slutpoäng
    print(f"You hit {points(targets)} of {len(targets)} targets") # poäng resultat 

# Starta spelet
play_game()
