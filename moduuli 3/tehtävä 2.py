hyttiluokka = input("Anna hyttiluokka (LUX,A,B,C): ")

if hyttiluokka == "LUX":
    print("parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("ikkunallinen hytti yläkannella.")
elif hyttiluokka == "B":
    print("ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("ikkunaton hytti autokannen alapuolella.")
else:
    print("virheellinen hyttiluokka")