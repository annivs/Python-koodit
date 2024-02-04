import random

def heita_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

# Pääohjelma
try:
    tahkojen_maara = int(input("Syötä nopan tahkojen yhteismäärä: "))
    maksimisilmaluku = int(input(f"Syötä nopan maksimisilmäluku (1..{tahkojen_maara}): "))

    if 1 <= maksimisilmaluku <= tahkojen_maara:
        while True:
            silmaluku = heita_noppaa(tahkojen_maara)
            print(f"Heitto: {silmaluku}")

            if silmaluku == maksimisilmaluku:
                print(f"Silmäluku {maksimisilmaluku} saavutettu!")
                break
    else:
        print("Virheellinen maksimisilmäluku.")
except ValueError:
    print("Virheellinen syöte, syötä kokonaisluku.")
