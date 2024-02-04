def laske_summa(lista):
    return sum(lista)

if __name__ == "__main__":
    try:

        luku_lista = [int(x) for x in input("Syötä kokonaislukuja pilkulla eroteltuna: ").split(',')]

        summa = laske_summa(luku_lista)
        print(f"Listan summa: {summa}")
    except ValueError:
        print("Virheellinen syöte, syötä kokonaislukuja pilkulla eroteltuna.")
