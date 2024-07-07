def cantidad():
    valor=int(input("Digite cantidad: "))
    if valor<=2:
        print("NO HAY DESCUENTO")
    if valor>2.01 and valor<=5:
        print("DESCUENTO 10%")
    if valor>5.01 and valor<=10:
        print("DESCUENTO 15%")
    if valor>10.01:
        print("DESCUENTO 20%")
cantidad()