import math

def laske_yksikkohinta(halkaisija, hinta):
    pizzan_pinta_ala = (math.pi * (halkaisija / 2)**2) / 10000
    yksikkohinta = hinta / pizzan_pinta_ala
    return yksikkohinta


try:

    halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Syötä ensimmäisen pizzan hinta (euroa): "))


    halkaisija2 = float(input("Syötä toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä toisen pizzan hinta (euroa): "))


    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)


    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat ovat samanhintaisia per neliömetri.")
except ValueError:
    print("Virheellinen syöte, syötä desimaalilukuja.")
