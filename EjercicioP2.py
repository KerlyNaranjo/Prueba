#EJERCICIO2: Ingresar números hasta que el usuario presione 0 y 
#retornar el promedio de los números

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
