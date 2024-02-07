user_input = input("lisätäänkö vai haetaanko lentoaseman vai lopettaa ohjelman (komennot: lisää/hae/lopeta)? ")

while True:
    if user_input == "lisää":
        ICAO_code = input("Anna ICAO- koodi: ")
        lentoasema_nimi = input("Anna lentoaseman nimi: ")
        lentoasema_tiedot = input("Anna lentoaseman tiedot: ")
        user_input = input("Haluatko lisätä vai hakea?")
    if user_input == "hae":
        ICAO_code_haku = input("Anna ICAO_ koodi: ")
        if ICAO_code_haku in lentoasema_tiedot:
            print(f"Lentoaseman nimi: {lentoasema_tiedot[ICAO_code_haku]}")
        else:
            print("Lentokenttää ei löytynyt.")
        user_input= input("Haluatko lisätä vai hakea?")
    if user_input == "lopeta":
        print("Ohjelma lopetetaan.")
        break

