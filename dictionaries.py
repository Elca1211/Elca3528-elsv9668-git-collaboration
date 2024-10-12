# [M5CN] Experimentera med ordlistor

# ordlistan users över användarnamnen (nyckel:värde)
users = {"nisse":"apa", "bosse":"ko", "stina":"t-rex"}

# skriver ut användarnamnen (nycklarna i ordlistan users)
print("Användare:\n")
for user in users: 
    print(f" {user}")

# skriver ut alla användarnamn och dess lösenord (nyckel och värde)
print("\nAnvändare och lösenord:\n")
for user, password in users.items():
    print(f"  {user}) {password}")
    
# skapar en ordlista med stränglistor som värden
data = {
    "nisse": ["luva", "vante"],
    "bosse":["spik", "skruv", "hammare"],
    "stina":["tidsmaskin"]}

# skriver ut alla anväbdarnamn (nyckel) med dess tillhörande värden
print("\nAnvändare och deras data:\n")
for user, items in data.items():
    print(f"  {user}) {items}")


# Slå upp användare, input till inmataren 
search_user = input("\n\nSlå upp användare: ")

# kontrollerar om användaren som skrevs in finns med i users. 
if search_user in data:
    # om användaren finns skrivs namnet och dess värden ut
    print(f"\nData lagrat för {search_user}: {data[search_user]}") 
else:
    # om namnet inte finns får inmataren ett meddelande att namnet den skrev inte finns
    print(f"\nAnvändaren {search_user} finns inte")
