# -*- coding: cp1252 -*-
# laittaa tiedoston sanoja.txt sanat j�rjestykseen ja tulostaa ne omille riveilleen  
# tiedosto = open("sanoja.txt","r")
sanoja = [line.rstrip('\n') for line in open("sanoja.txt","r")]
sanoja.sort()
print("Sanat laitettuna aakkosj�rjestykseen: ")
for i in sanoja:
	print(i)
