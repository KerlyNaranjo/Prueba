#ngresar números hasta que el usuario presione 0 y 
#retornar el promedio de los números

#Menu
#def menu():
#	print()

print ('\t\t\t\t\n        PRUEBA\n')
print (' AUTORES: Kerly Naranjo')
print ('          Katherine Lasluisa\n\t  Javier Chamba\n\t  Jazmin Villamarin')

print ('\nEscoja el numero de ejercicio: \n')
print ('1. Suma de vectores x, y, z')
print ('2. Promedio de numeros')
print ('3. Imvertir el contenido de un archivo')
print ('4. Salir')

opt = int(input("\nLa opcion es: "))

if opt == 1:
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

elif opt == 2:
	#Agregar funcion
	print(" ")

elif opt == 3:
	#Agregar funcion
	print(" ")

elif opt == 4:
	exit()
