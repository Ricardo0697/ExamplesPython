#importar la clase math para poder utilizar las funciones o constantes de
#de la clase como: sqrt,pi, pow,e
import math
d= int(input("Digite el Diametro del cilindro: "))
h= int(input("Digite la altura del cilindro: "))
#formula del volumen: PI * r2 * h
r= d/2.0
v= math.pi * r**2 * h
print("El volumen del Objeto es de; ",v)
