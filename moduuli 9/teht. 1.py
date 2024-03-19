class Auto:

    auto_count = 0

    def __init__(self, rekkari, huippunopeus):
        Auto.auto_count = Auto.auto_count + 1
        print(f"Uusi auto, autoja on nyt {Auto.auto_count} kpl")
        self.rekkari = rekkari
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus = huippunopeus

    def print_info(self):
        print(f"{self.rekkari} {self.huippunopeus}")
        print(f"{self.nopeus} {self.matka}")

auto1 = Auto("ABC-123", "142")

print(f"Uuden auton tiedot {auto1.print_info}")

auto1.print_info()