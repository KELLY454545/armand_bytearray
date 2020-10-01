#!/usr/bin/env python3

#fonction Counter() pour compter les élements dans un tableau
from collections import Counter


def p_pair( b_array):
	#b_array doit être un bytearray

	bit = bytearray()

	for i in range(len(b_array)):
		#convertion en binaire
		octet = bin(b_array[i])[2:]


		if (Counter(octet)['1'] % 2 == 0):
			#le nombre de 1 est pair
			res.append(int('0' + octet,2))
		else:
			#le nombre de 1 est impair
			res.append(int('1' + octet,2))
	return bit
	



def p_impair(b_array):
	#b_array doit être un bytearray
	bit = bytearray()
	for i in range(len(b_array)):
     #boucle qui permet de parcourir le tableau
                #convertion en binaire
                octet = bin(b_array[i])[2:]


                if (Counter(octet)['1'] % 2 == 0):
                    
                        res.append(int('1' + octet,2))
                else:
                        res.append(int('0' + octet,2))

	return bit
