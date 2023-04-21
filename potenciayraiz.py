import math
numero= int(input("Digite un numero: "))
if numero>=1:
   resultado=math.sqrt(numero)
   print("la raiz de ese numero es:",resultado)
else:
    potencia1=math.pow(numero,2)
    potencia2=math.pow(numero,3)
    print("las potencias elevas al dos y a la tres equivalentemente son: ",potencia1,potencia2)



