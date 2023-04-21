tiquete= int(input("Cantidad de Tiquetes que desea comprar: "))
precio= 10000*tiquete
if tiquete==1:
    print("Su pago es:",precio)
elif tiquete==2:
    print("su pago es de ",precio*0.10)
elif tiquete==3:
    print("su pago es de ",precio*0.15)
elif tiquete==4:
    print("su pago es de ",precio*0.20)
    if tiquete<=5:
        print("no puede Comprar mas de Cinco Gracias por su compra ")
    else:
        print("No muede comprar mas de cinco")

