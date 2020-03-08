import time		

tiedostonimi = "muistio.txt"
def aika():
    aika = time.strftime("%X %x")
    return aika
def luetiedosto(nimi = "muistio.txt"):
    try:
        tiedosto = open(tiedostonimi,"r")
        teksti = tiedosto.read()
        tiedosto.close()
        return teksti
    except Exception:
        print("Tiedostoa ei löydy, luodaan tiedosto.")
        tiedosto = open(tiedostonimi,"w")
        tiedosto.close()
        tiedosto = open(tiedostonimi,"r")
        teksti = tiedosto.read()
        tiedosto.close()
        return teksti

valinta = 0
def aloitus():
    try:
        tiedosto = open(tiedostonimi,"r")
        teksti = tiedosto.read()
        tiedosto.close()
        return teksti
    except Exception:
        print("Oletusmuistioa ei löydy, luodaan tiedosto.")
        tiedosto = open(tiedostonimi,"w")
        tiedosto.close()
        tiedosto = open(tiedostonimi,"r")
        teksti = tiedosto.read()
        tiedosto.close()
        return teksti
aloitus()
while valinta != "5":
    print("Käytetään muistiota:",tiedostonimi,"""
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta\n""")
    valinta = input("Mitä haluat tehdä?: ")
    if valinta == "1":	
            teksti = luetiedosto()
            print(teksti)

    elif valinta == "2":
            uusimerkinta = input("Kirjoita uusi merkintä: ")
            uusimerkinta = uusimerkinta +  ":::" + aika() + "\n"
            tiedosto = open(tiedostonimi,"a")
            tiedosto.write(uusimerkinta)
            tiedosto.close()
    elif valinta == "3":
            tiedosto = open(tiedostonimi,"w")
            print("Muistio tyhjennetty.")
            tiedosto.close()	    
    elif valinta == "4":
            tiedostonimi = input("Anna tiedoston nimi:")
            teksti = luetiedosto()
    elif valinta == "5":
            print("Lopetetaan.")
    else:
            continue
