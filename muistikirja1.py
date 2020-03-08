import time		
aika = time.strftime("%X %x")
tiedostonimi = "muistio.txt"
valinta = 0
while valinta != "4":
    print("""(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta\n""")
    valinta = input("Mitä haluat tehdä?: ")
    if valinta == "1":	
            tiedosto = open(tiedostonimi,"r")
            teksti = tiedosto.read()
            print(teksti)
            tiedosto.close()
    elif valinta == "2":
            uusimerkinta = input("Kirjoita uusi merkintä: ")
            uusimerkinta = uusimerkinta +  ":::" + aika
            tiedosto = open(tiedostonimi,"a")
            tiedosto.write(uusimerkinta)
            tiedosto.close()
    elif valinta == "3":
            tiedosto = open(tiedostonimi,"w")
            print("Muistio tyhjennetty.")
            tiedosto.close()	    
    elif valinta == "4":
	    print("Lopetetaan.")			
    else:
            continue
