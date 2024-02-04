
luvut = []

while True:
    syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")


    if syote == "":
        break
    try:
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte, syötä kokonaisluku.")

luvut.sort(reverse=True)

print("Viisi suurinta lukua suuruusjärjestyksessä:")
for i in range(min(5, len(luvut))):
    print(luvut[i])
