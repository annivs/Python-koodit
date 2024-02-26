import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="root",
    password="root",
    autocommit=True
)


def airport_search_by_icao_code():
    cursor = connection.cursor()
    icao_search = input("Anna lentokentän ICAO-tunnus:\n ").upper()
    cursor.execute(f"SELECT name FROM airport WHERE ident='{icao_search}'")
    result = cursor.fetchone()

    if result:
        print(f"Lentokentän nimi on {result[0]}.")

    else:
        print("Lentokenttää ei löytynyt.")


airport_search_by_icao_code()

