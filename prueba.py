def suma():
	for i in range(len(vector1)):
		print (vector1[i] + vector2[i])
	print (" ")

vector1= [ ]
elemen_lista = 2
print ("PRIMER VECTOR")
for i in range(elemen_lista + 1):
	valores = int(input("INTRODUZCA EL VALOR DEL ELEMENTO: "))
	vector1.append(valores)
print ("VECTOR 1: "+str(vector1))

vector2 = [ ]
elemen_lista2 = 2
print ("SEGUNDO VECTOR")
for i in range(elemen_lista2 + 1):
	valores = int(input("INTRODUZCA EL VALOR DEL ELEMENTO: "))
	vector2.append(valores)
print ("VECTOR 2: "+str(vector2))



suma()



