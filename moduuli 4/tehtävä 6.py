import random


def calculate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Tarkistetaan, onko piste yksikköympyrän sisällä
        if x ** 2 + y ** 2 < 1:
            inside_circle += 1

    pi_approximation = 4 * inside_circle / num_points
    return pi_approximation


def main():
    try:
        num_points = int(input("Syötä arvottavien pisteiden määrä: "))
        if num_points <= 0:
            raise ValueError("Luku on oltava positiivinen.")

        pi_approximation = calculate_pi(num_points)

        print(f"Piin likiarvo {num_points} pisteellä on: {pi_approximation}")

    except ValueError as e:
        print(f"Virheellinen syöte: {e}")
    except Exception as e:
        print(f"Ohjelman suorituksessa tapahtui virhe: {e}")


if __name__ == "__main__":
    main()
