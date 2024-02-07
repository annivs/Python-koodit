nimet = set()

while True:
    nimi = input("Syötä nimi (tyhjä rivi lopettaa): ")
    if not nimi:
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print(nimet)