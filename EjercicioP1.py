#Suma de vectores x, y, z: Ingresar dos vectores 
#(x1, y1, z1) y (x2, y2, z2)y sumar sus valores: (x1+x2,y1+y2, z1+z2)

print('\n\t\tSUMA DE VECTORES ')

print('\nIngrese valores para el vector 1: ')
a = int(input('Valor 1: '))
b = int(input('Valor 2: '))
c = int(input('Valor 3: '))

print('\nIngrese valores para el vector 2: ')
d = int(input('Valor 1: '))
e = int(input('Valor 2: '))
f = int(input('Valor 3: '))

v1 = [a,b,c]
v2 = [d,e,f]

suma = [a+d, b+e, c+f]

print('\nLa suma = ' + str(suma))
