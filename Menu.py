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


encabezado()
opt = int(input("\nLa opcion es: "))

if opt == 1:
	ejercicio1()
	
if opt == 2:
	ejercicio2()

if opt == 3:
	#Agregar funcion
	print(" ")

if opt == 4:
	exit()

