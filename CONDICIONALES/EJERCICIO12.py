def valor():
    valor = float(input("Digite promedio: "))
    valorm= float(input("Digite valor: "))
    operacion=float()
    operacionf=float()
    if valor>=4.5:
        print("DESCUENTO 30%")
        operacion=valorm*0.3
        operacionf=valorm-operacion
    else:
        print("NO HAY DESCUENTO")
        operacion=valorm*0.1
        operacionf=valorm+operacion
    print("NOTA: ",valor)
    print("VALOR A PAGAR: ",operacionf)

valor()