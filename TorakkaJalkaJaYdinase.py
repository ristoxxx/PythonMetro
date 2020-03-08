import random
def main():
	kierrokset = 0
	valinta = 0
	ppisteet = 0
	tpisteet = 0
	tppisteet = 0
	while valinta != "Lopeta":
		valinta = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa): ")
		if valinta == "Lopeta":
			break	
		satunnainen = random.randint(0,3)
		kierrokset = kierrokset + 1
		if satunnainen == 1:
			tietokone = "Jalka"
		elif satunnainen == 2:
			tietokone = "Ydinase"
		elif satunnainen == 0 or 3:
			tietokone = "Torakka"
		print("Sinä valitsit:", valinta)
		print("tietokone valitsi:", tietokone)
		if valinta == tietokone:
			print("Tasapeli!")
			tppisteet = tppisteet + 1
		elif valinta == "Jalka" and tietokone == "Ydinase":
			print("Hävisit!")
			tpisteet = tpisteet + 1
		elif valinta == "Jalka" and tietokone == "Torakka":
			print("Voitit!")
			ppisteet = ppisteet + 1
		elif valinta == "Torakka" and tietokone == "Jalka":
			print("Hävisit!")
			tpisteet = tpisteet + 1
		elif valinta == "Torakka" and tietokone == "Ydinase":
			print("Voitit!")
			ppisteet = ppisteet + 1
		elif valinta == "Ydinase" and tietokone == "Torakka":
			print("Hävisit!")
			tpisteet = tpisteet + 1
		elif valinta == "Ydinase" and tietokone == "Jalka":
			print("Voitit!")
			ppisteet = ppisteet + 1
		
	print("Pelasit",kierrokset,"kierrosta, joista voitit",ppisteet,"ja pelasit tasan",tppisteet,"peliä.")
	return 0
main()
