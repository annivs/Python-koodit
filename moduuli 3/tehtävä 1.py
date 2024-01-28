kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä"))
if kuhan_pituus < 37:
    puuttuva_pituus =37 - kuhan_pituus
    print(f"Kuha on alimittainen. Puuttuu {puuttuva_pituus} cm halutusta pituudesta. Laske kuha takaisin järveen.")

else:
    print("Kuha on sallitun mittainen. Voit pitää sen.")

