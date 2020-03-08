# -*- coding: cp1252 -*-
# laittaa tiedoston sanoja.txt sanat järjestykseen ja tulostaa ne omille riveilleen  
# tiedosto = open("sanoja.txt","r")
sanoja = [line.rstrip('\n') for line in open("sanoja.txt","r")]
sanoja.sort()
print("Sanat laitettuna aakkosjärjestykseen: ")
for i in sanoja:
	print(i)
