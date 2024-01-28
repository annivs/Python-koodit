while True:
        tuumat = float(input("Syötä tuumat: "))
        if tuumat < 0:
            break
        senttimetrit = tuumat * 2.54
        print(f"{tuumat} tuumaa on {senttimetrit:.2f} senttimetriä.")

