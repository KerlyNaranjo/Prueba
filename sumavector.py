
#suma de vectores
import math
vector11=int(input("x1:"))
vector12=int(input("y1:"))
vector13=int(input("z1:"))
#
vector21=int(input("x2:"))
vector22=int(input("y2:"))
vector23=int(input("z2:"))
def suma():
	suma1=vector11+ vector21
	suma2= vector12+ vector22
	suma3= vector13+ vector23
	sumap=suma1,suma2,suma3
	print("los numeros de la suma son:"+ str(sumap))

suma()
