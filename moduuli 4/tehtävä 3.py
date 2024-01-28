numerot = []

while True:
    syöte = input("Syötä luku: ")

    if not syöte:
        break

    try:
        luku = float(syöte)
        numerot.append(luku)
    except ValueError:
        print("Virheellinen syöte. Anna luku.")

if numerot:
    pienin = min(numerot)
    suurin = max(numerot)

    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")



