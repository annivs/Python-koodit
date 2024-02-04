def muunna_gallonoista_litroiksi(gallonoita):
    litrat = gallonoita * 3.785
    return litrat

while True:
    try:
        gallonoita = float(input("Syötä bensiinin määrä Yhdysvaltain nestegallonoina (negatiivinen lopettaa): "))

        if gallonoita < 0:
            print("Ohjelma lopetetaan.")
            break

        litrat = muunna_gallonoista_litroiksi(gallonoita)
        print(f"{gallonoita} nestegallonaa on {litrat} litraa.")
    except ValueError:
        print("Virheellinen syöte, syötä desimaaliluku.")