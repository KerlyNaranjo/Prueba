#import os
archivo=open("Narvaez.txt","r")
context=archivo.read()
print("ARCHIVO ORIGINAL (#DE PALABRAS): " + str(len(context.split(" "))))
print("-----------------------------------")
pr1=context[0:56999]
pr2=context[56999:113998]
pr3=context[113999:]

p1=open("File1.txt","w")
p1.write(pr1)
p1=open("File1.txt","r")
a=p1.read()
print("Archivo1 (#DE PALABRAS): " + str(len(a.split(" "))))
#print("La cadena invertida es:",a[::-1])
p1.close()
print("-----------------------------------")

p2=open("File2.txt","w")
p2.write(pr2)
p2=open("File2.txt","r")
b=p2.read()
print("Archivo2 (#DE PALABRAS): " + str(len(b.split(" "))))


p2.close()
print("-----------------------------------")

p3=open("File3.txt","w")
p3.write(pr3)
p3=open("File3.txt","r")
c=p3.read()
print("Archivo3 (#DE PALABRAS): " + str(len(c.split(" "))))
i1=a[::-1]

p3.close()
print("-----------------------------------")



