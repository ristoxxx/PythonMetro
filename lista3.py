def lisaa():
	lisattava = input("Mitä lisätään?: ")
	return lisattava

def poista(lista):
	print("Listalla on",len(lista),"alkiota.")
	poistettava = input("Monesko niistä poistetaan?: ")
	return poistettava

def listaa(lista):
	print("Listalla oli tuotteet:")
	for i in lista:
		print(i)

def valikko():
	valinta = input("""Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: """)
	return valinta

def main():
	lista = []
	valinta = 0
	while valinta != "3":
		valinta = valikko()
		if valinta == "1":
			lista.append(lisaa())					
		elif valinta == "2":
			try:
				lista.pop(int(poista(lista)) - 1)
			except Exception:
				print("Virheellinen valinta.")
				
		elif valinta == "3":
			listaa(lista)
		else:
			print("Virheellinen valinta.")


main()
