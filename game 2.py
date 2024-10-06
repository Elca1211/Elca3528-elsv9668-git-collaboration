from random import randint

# Funktioner vi redan har skapat
def splash():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("              Biathlon")
    print()
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def new_targets():
    return [0, 0, 0, 0, 0]

def is_open(target):
    return target == 0

def is_closed(target):
    return target == 1

def close_target(targets, position):
    if is_open(targets[position]):
        targets[position] = 1

def random_hit():
    return randint(0, 1) == 1

def shoot(targets, position):
    if is_closed(targets[position]):
        return "Hit on closed target"
    elif random_hit():
        close_target(targets, position)
        return "Hit on open target"
    else:
        return "Miss"

def targets_to_string(targets):
    return " ".join('*' if is_closed(t) else 'O' for t in targets)

def view_targets(targets):
    print("\n  0 1 2 3 4\n")
    print("  " + targets_to_string(targets) + "\n")

def points(targets):
    return sum(1 for t in targets if is_closed(t))

# Ny funktion för att parsa användarinmatning
def parse_target(string):
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
