
sukupuoli = input("Anna biologinen sukupuolesi ('nainen' tai 'mies'): ")
hemoglobiiniarvo = float(input("Anna hemoglobiiniarvo (g/l): "))


if 'nainen':
        if 117 <= hemoglobiiniarvo <= 175:
            print("Hemoglobiiniarvo on normaali.")
        elif hemoglobiiniarvo < 117:
            print("Hemoglobiiniarvo on alhainen.")
        else:
            print("Hemoglobiiniarvo on korkea.")

if 'mies':
        if 134 <= hemoglobiiniarvo <= 195:
            print("Hemoglobiiniarvo on normaali.")
        elif hemoglobiiniarvo < 134:
            print("Hemoglobiiniarvo on alhainen.")
        else:
            print("Hemoglobiiniarvo on korkea.")


