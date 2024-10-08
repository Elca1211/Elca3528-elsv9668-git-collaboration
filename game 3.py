
# BIATHLON A HIT OR MISS GAME 

#-----------------------------------------------------------------------------------
# Funktioner
#-----------------------------------------------------------------------------------

# Importera nödvändiga moduler och funktioner

from random import randint  # Importerar funktionen randint från python-modulen random för att generera slumpmässiga heltal (används senare i "random_hit()")


def splash():
    # Skriver ut spelets titel och introduktion
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon")
    print()
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") # Inget returvärde, ingen sidoeffekt annat än att visa information för spelaren.


def new_targets():
    # Skapar en ny måltavla representerad som en lista med fem öppna mål ([0, 0, 0, 0, 0]). (Öppet mål = 0) 
    return [0, 0, 0, 0, 0] # Returnerar en listan till spelaren. 


def is_open(target): # Kontrollerar om ett mål är öppet (0)
    return target == 0


def is_closed(target):
    # Kontrollerar om ett mål är stängt (1)
    return target == 1


def close_target(targets, position):
    # Stänger ett mål (ändrar värdet från 0 till 1) vid angiven position om det är öppet.
    if is_open(targets[position]):
        targets[position] = 1 # om det är öppet ändras måltavlan vid den positionen till 1, dvs målet är stängt


def random_hit():
    # Returnerar True med 50% sannolikhet (träff) och False med 50% sannolikhet (miss)
    return randint(0, 1) == 1 # Gör spelet mer förutsägbart

def shoot(targets, position): # Hanterar skott mot ett specifikt mål baserat på en slumphändelse, retuneras strängar 
    if is_closed(targets[position]): # Om man träffar ett stängt mål 
        return "Hit on closed target"
    elif random_hit(): # 50 % chans för träff om man skjuter mot ett öppet mål (random_hit() = True)
        close_target(targets, position) # Om man träffar ett öppet mål
        return "Hit on open target" 
    else:
        return "Miss" # Om man siktar mot ett öppet mål, men missar pågrund av slumpen, retuneras strängen "Miss" (random_hit() = False)


######### ÄNDRA ###################################################################
def targets_to_string(targets):
    result = ""
    for target in targets:
        if is_closed(target):  # Om målet är stängt
            result += "* " # antalet träffar
        else:  # Om målet är öppet
            result += "0 " # antalet missar 
    return result  # Returnerar den formaterade strängen


# def targets_to_string(targets):
#     # Retunerar måltavlan till den resulterande måltavlan efter varje skott. 
#     return " ".join('*' if is_closed(t) else 'O' for t in targets) # * = stängt mål (träff) och O = öppet mål BY HAND
# # t är elementet i listan 
# # join utesluter [] och har ett blanksteg innan. 

###################################################################################



def view_targets(targets): 
    print("\n  1 2 3 4 5\n") # Skriver ut listan med de numrerade positionerna (\n = blank rad) 
    print("  " + targets_to_string(targets) + "\n") # Skriver ut måltavlan 





######### ÄNDRA ###################################################################
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
###################################################################################



######### ÄNDRA ###################################################################
# Ny funktion för att parsa användarinmatning 
def parse_target(string): # Omvandlar de verkliga indexen (0-4) till (1-5) från spelarens input
    if len(string) == 1 and string.isnumeric(): # omvandlar till ett tal 
        num = int(string) # ex om spelaren skriver 3 omvandlas det till 3 
        if 1 <= num <= 5: # talen 1-5
            return num - 1 # Omvandlingen från verkliga index, ex om man skriver 1: 1-1=0 som är index [0]
    return None

####################################################################################


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
            continue ###############FÖRSTÅ!!!!!!!!
        
        result = shoot(targets, position)
        print(result)
        view_targets(targets)

    # När alla skott är slut, visa slutpoäng
    print(f"You hit {points(targets)} of {len(targets)} targets") # poäng resultat 

# Starta spelet
play_game()
#-----------------------------------------------------------------------------------
# Spel för två spelare
#-----------------------------------------------------------------------------------
# def play_game_two_players():
#     splash()  # Visa spelets titel och introduktion
#     shots = 5  # Antal skott per spelare
#     players = ["Player A", "Player B"]  # Lista över spelare
#     targets = [new_targets(), new_targets()]  # Skapa måltavlor för båda spelarna
#     current_shot = 0  # Skott räknare
# 
#     while current_shot < shots:
#         for i, player in enumerate(players):
#             current_shot += 1
#             print(f"{player}'s turn")
#             view_targets(targets[i])
#             position = parse_target(input(f"Shot nr {current_shot} at: "))
#             if position is None:
#                 print("Please enter a valid position between 1 and 5.")
#                 continue
#             
#             result = shoot(targets[i], position)
#             print(result)
#             view_targets(targets[i])
# 
#     for i, player in enumerate(players):
#         print(f"{player} hit {points(targets[i])} of {len(targets[i])} targets")
# 
# # Starta spelet för två spelare
# play_game_two_players()
