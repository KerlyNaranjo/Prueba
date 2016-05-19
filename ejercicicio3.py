#import os
archivo=open("Narvaez.txt","r")
context=archivo.read()
print("Numero de palabras: " + str(len(context.split(" "))))

pr1=context[0:56999]
pr2=context[56999:113998]
pr3=context[113999:]

p1=open("File1.txt","w")
p1.write(pr1)
p1=open("File1.txt","r")
a=p1.read()
a.reverse()
print (str(a))
print("Archivo1: " + str(len(a.split(" "))))
p1.close()

p2=open("File2.txt","w")
p2.write(pr2)
p2=open("File2.txt","r")
b=p2.read()
print("Archivo2: " + str(len(b.split(" "))))
p2.close()

p3=open("File3.txt","w")
p3.write(pr3)
p3=open("File3.txt","r")
c=p3.read()
print("Archivo3: " + str(len(c.split(" "))))
p3.close()



