class Auto:

    auto_count = 0

    def __init__(self, rekkari, huippunopeus, alkunopeus, kuljettu_matka):
        Auto.auto_count = Auto.auto_count + 1
        print(f"Uusi auto, autoja on nyt {Auto.auto_count} kpl")
        self.rekkari = rekkari
        self.nopeus = 0
        self.kuljettu_matka = 0
        self.huippunopeus = huippunopeus


    def print_info(self):
        print(f"{self.rekkari} {self.huippunopeus}")
        print(f"{self.nopeus} {self.kuljettu_matka}")

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, aika):
        self.kuljettu_matka += self.nopeus * aika



auto = Auto('ABC-123',150, 60, 2000)
    #kiihdytys
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Auton uusi nopeus:", auto.nopeus, "km/h")

    #hätäjarrutus
auto.kiihdytä(-200)
print("Auton nopeus hätäjarrutuksen jälkeen:", auto.nopeus, "km/h")

auto.kulje(1.5)
auto.print_info()