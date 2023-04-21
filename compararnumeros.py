a1 = int(input("Digite el valor de A: "))
b1 = int(input("Digite el valor de B: "))
c1 = int(input("Digite el valor de C: "))
if a1 == b1 and b1 == c1 and c1 == a1:
    print("ERROR NO DIGITE NINGUNO IGUAL")
elif a1 > b1:
    if b1 > c1:
        print("A es mayor y C es menor")
    else:
        print("C es el mayor y el B es el menor")
elif b1 > c1:
    if a1 < c1:
        print("B es mayor y C es el menor")

elif c1 > b1:
    if c1 > a1:
        print("C es mayor y A es el menor")
    else:
        print("Final del Programa")
