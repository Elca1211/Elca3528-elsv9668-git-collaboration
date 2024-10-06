 # spelet med kommentarer

# Importera nödvändiga moduler och funktioner
from random import randint  # Importerar funktionen randint från modulen random för att generera slumpmässiga heltal

# Funktioner vi redan har skapat
def splash():
    # Visar spelets titel och introduktion
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon")
    print()
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def new_targets():
    # Skapar en ny måltavla med fem öppna mål (representerade av 0)
    return [0, 0, 0, 0, 0]

def is_open(target):
    # Kontrollerar om ett mål är öppet (0)
    return target == 0

def is_closed(target):
    # Kontrollerar om ett mål är stängt (1)
    return target == 1

def close_target(targets, position):
    # Stänger ett mål om det är öppet
    if is_open(targets[position]):
        targets[position] = 1

def random_hit():
    # Returnerar True med 50% sannolikhet (träff) och False med 50% sannolikhet (miss)
    return randint(0, 1) == 1

def shoot(targets, position):
    # Hanterar skott på ett mål och returnerar resultatet
    if is_closed(targets[position]):
        return "Hit on closed target"
    elif random_hit():
        close_target(targets, position)
        return "Hit on open target"
    else:
        return "Miss"

def targets_to_string(targets):
    # Konverterar måltavlan till en strängrepresentation för visning
    return " ".join('*' if is_closed(t) else 'O' for t in targets)

def view_targets(targets):
    # Visar måltavlan på skärmen
    print("\n  1 2 3 4 5\n")
    print("  " + targets_to_string(targets) + "\n")

def points(targets):
    # Räknar antalet stängda mål och returnerar poängen
    return sum(1 for t in targets if is_closed(t))

# Ny funktion för att parsa användarinmatning
def parse_target(string):        # utför någon form av logik
    # Konverterar en sträng till motsvarande index i måltavlan
    if len(string) == 1 and string.isnumeric():
        num = int(string)
        if 1 <= num <= 5:
            return num - 1
    return None

# Huvudspel loop
def play_game():
    splash()  # Visa spelets titel och introduktion
    shots = 5  # Antal skott
    current_shot = 0  # Skott räknare
    targets = new_targets()  # Skapa ny måltavla
    view_targets(targets)  # Visa måltavlan

    while current_shot < shots:
        current_shot += 1
        position = parse_target(input(f"Shot nr {current_shot} at: "))
        if position is None:
            print("Please enter a valid position between 1 and 5.")
            continue
        
        result = shoot(targets, position)
        print(result)
        view_targets(targets)

    # När alla skott är slut, visa slutpoäng
    print(f"You hit {points(targets)} of {len(targets)} targets")

# Starta spelet
play_game()

#-------------------------------------------------------------

def play_game_two_players():
    splash()  # Visa spelets titel och introduktion
    shots = 5  # Antal skott per spelare
    players = ["Player A", "Player B"]  # Lista över spelare
    targets = [new_targets(), new_targets()]  # Skapa måltavlor för båda spelarna
    current_shot = 0  # Skott räknare

    while current_shot < shots:
        for i, player in enumerate(players):
            current_shot += 1
            print(f"{player}'s turn")
            view_targets(targets[i])
            position = parse_target(input(f"Shot nr {current_shot} at: "))
            if position is None:
                print("Please enter a valid position between 1 and 5.")
                continue
            
            result = shoot(targets[i], position)
            print(result)
            view_targets(targets[i])

    for i, player in enumerate(players):
        print(f"{player} hit {points(targets[i])} of {len(targets[i])} targets")

# Starta spelet för två spelare
play_game_two_players()
