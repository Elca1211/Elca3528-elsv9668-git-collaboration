# Programmet skall sedan skriva ut alla element i listan names
# på en egen rad. Raderna skall numreras med start från 1.

names = ["nisse", "stina", "bosse", "mimmi"] # Skapar listan

n = 1 # Variabel som håller koll på rad-numret

# For slinga som kör 4 ggr och skriver ut alla namn med numrering
for name in names:
    print(f" {n}) {name}\n")
    n += 1
