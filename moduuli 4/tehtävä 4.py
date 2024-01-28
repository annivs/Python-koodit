import random
def arvaa_luku():
    oikea_luku = random.randint(1, 10)
    arvaukset = 0

    while True:
        try:
            pelaajan_arvaus = int(input("Arvaa luku väliltä 1..10: "))

            if 1 <= pelaajan_arvaus <= 10:
                arvaukset += 1

                if pelaajan_arvaus < oikea_luku:
                    print("Liian pieni arvaus.")
                elif pelaajan_arvaus > oikea_luku:
                    print("Liian suuri arvaus.")
                else:
                    print(f"Oikein! Arvasit oikean luvun {arvaukset} arvauksella.")
                    break
            else:
                print("Anna luku väliltä 1..10.")
        except ValueError:
            print("Virheellinen syöte. Anna kokonaisluku:")

arvaa_luku()