def on_karkausvuosi(vuosi):
    if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
        return True
    else:
        return False

luku = input("Syötä vuosiluku: ")
vuosi = int(luku)
if vuosi >=0:
    if on_karkausvuosi(vuosi):
        print(f" {vuosi} on karkausvuosi.")
    else:
        print(f" {vuosi} ei ole karkausvuosi.")
else:
        print("Anna positiivinen vuosiluku ")




