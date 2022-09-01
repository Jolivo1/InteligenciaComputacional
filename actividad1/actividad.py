#Area de un Cuadrado#
from cmath import sqrt
import math


a=float(input("ingrese el lado del cuadrado\n"))
area=a*a
print(str(area))
#De un triangulo rectangulo ABC, se conocen los catetos b = 33 c = 21 resolver el triangulo#

b = 33 
c = 21
r =  math.sqrt(b**2 + c**2)  
print(r)

#Calcular la formula general en python#
a = float(input("Ingrese numero a"))
b = float(input("Ingrese numero b"))
c = float(input("Ingrese numero c"))

x=b**2-4*a*c
if x<0:
 print('no existe solucion')
else:
    x1=(-b+math.sqrt(x))/2*a
    x2=(-b-math.sqrt(x))/2*a
    print('x1=',x1)
    print('x2=',x2)



print('positivo o negativo',x)

##Calcular el area de un circulo cuyo radio es ogial a 20cm##

print ("Area Circulo")
pi = 3.1415
area = ((20**2) * pi)
print(f"El area es: {area}cm2")

