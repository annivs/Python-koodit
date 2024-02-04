import random

def heita_arpakuutiot(luku):
    summa = 0
    for _ in range(luku):
        silmaluku = random.randint(1, 6)
        print(f"Heitto: {silmaluku}")
        summa += silmaluku
    return summa

def main():
    try:
        luku = int(input("Syötä noppien lukumäärä: "))
        if luku <= 0:
            print("Noppien lukumäärän tulee olla positiivinen.")
        else:
            kokonaissumma = heita_arpakuutiot(luku)
            print(f"\nKaikkien heittojen summa: {kokonaissumma}")
    except ValueError:
        print("Virheellinen syöte. Syötä positiivinen kokonaisluku.")

if __name__ == "__main__":
    main()