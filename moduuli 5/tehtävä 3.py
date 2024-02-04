def onko_alkuluku(luku):
    if luku < 2:
        return False
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            return False
    return True

try:
    syote = int(input("Syötä kokonaisluku: "))
    if onko_alkuluku(syote):
        print(f"{syote} on alkuluku.")
    else:
        print(f"{syote} ei ole alkuluku.")
except ValueError:
    print("Virheellinen syöte, syötä kokonaisluku.")
