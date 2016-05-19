#PRUEBA con EJERCICIO1 y EJERCICIO2

def ejercicio2():
	print('\nInstrucciones: 1. Ingresa los numeros que desees')
	print('               2.Cuando quieras terminar presiona 0\n')
	nums = int(input('Ingrese un número: '))
	cont = 0
	acum = 0

	while nums != 0:
		nums = int(input('Ingrese un número: '))
		cont = cont + 1
		acum = acum + nums

	promedio = acum / cont
	print('\nPromedio = ' + str(promedio))


def ejercicio1():
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
	#suma
	for i in range(len(vector1)):
		print (vector1[i] + vector2[i])


def encabezado():
	print ('\t\t\t\t\n        PRUEBA\n')
	print (' AUTORES: Kerly Naranjo')
	print ('          Katherine Lasluisa\n\t  Javier Chamba\n\t  Jazmin Villamarin')

	print ('\nEscoja el numero de ejercicio: \n')
	print ('1. Suma de vectores x, y, z')
	print ('2. Promedio de numeros')
	print ('3. Imvertir el contenido de un archivo')
	print ('4. Salir')

def ejercicio3():
	archivo = open('ArchiOriginal.txt','w')
	parte1 = archivo.write("hola como estas\n")
	parte2 = archivo.write("bien\n")
	parte3 = archivo.write("y tu\n")
	archivo.close()

	archivo = open('Parte1.txt','w')
	parte1 = archivo.write("hola como estas\n")
	archivo.close()

	archivo = open('Parte2.txt','w')
	parte1 = archivo.write("bien\n")
	archivo.close()

	archivo = open('Parte3.txt','w')
	parte1 = archivo.write("y tu\n")
	archivo.close()

	archivo = open('Parte1.txt','r')
	linea = archivo.readline()
	while linea!="":
		print (linea)
		print (linea[::-1])
		linea = archivo.readline()
	archivo.close()

	archivo = open('Parte2.txt','r')
	linea = archivo.readline()
	while linea!="":
		print (linea)
		print (linea[::-1])
		linea = archivo.readline()
	archivo.close()

	archivo = open('Parte3.txt','r')
	linea = archivo.readline()
	while linea!="":
		print (linea)
		print (linea[::-1])
		linea = archivo.readline()
	archivo.close()


encabezado()
opt = int(input("\nLa opcion es: "))

if opt == 1:
	ejercicio1()
	
if opt == 2:
	ejercicio2()

if opt == 3:
	ejercicio3()

if opt == 4:
	exit()

