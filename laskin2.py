# Yksinkertainen laskin jossa nelilaskimen lisäksi sin ja cos
import math
# Funktio kysyy käyttäjältä luvun tai tulostaa virheellinen syöte jos käyttäjä syöttää muuta kuin luvun
def kysely():
	luku = input("Anna luku: ")
	try:
		luku = int(luku)
		return luku
	except Exception:
		print("Virheellinen syöte!")
		kysely()
# Funktio suoritetaan kaksi kertaa jotta saadaan käyttäjältä kaksi lukua
ekaluku = kysely()
tokaluku = kysely()
# Suoritetaan kysely joka kysyy mikä laskutoimitus luvuille suoritetaan
# silmukka myös tulostaa luvut silmukkaa jatketaan kunnes käyttäjä syöttää luvun 8
valinta = 0
while valinta != "8":    
    print("""(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut:""",ekaluku,tokaluku)
    valinta = input("Tee valinta(1-8): ")
    if valinta == "1":
            tulos = int(ekaluku) + int(tokaluku)
            print("Tulos on: ", tulos)
    elif valinta == "2":
            tulos = int(ekaluku) - int(tokaluku)
            print("Tulos on: ", tulos)
    elif valinta == "3":
            tulos = int(ekaluku) * int(tokaluku)
            print("Tulos on: ", tulos)
    elif valinta == "4":
            tulos = int(ekaluku) / int(tokaluku)
            print("Tulos on: ", tulos)
    elif valinta == "5":
            tulos = math.sin(int(ekaluku)/int(tokaluku)) 
            print("Tulos on: ", tulos)
    elif valinta == "6":
            tulos = math.cos(int(ekaluku)/int(tokaluku)) 
            print("Tulos on: ", tulos)
    elif valinta == "7":
	    ekaluku = input("Anna uusi ensimmäinen luku: ")
	    tokaluku = input("Anna uusi toinen luku: ")	
    else:
        continue
