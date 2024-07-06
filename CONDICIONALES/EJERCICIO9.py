def alza():
    valor=float(input("Digite valor: "))
    operacion=float()
    operacionf=float()
    if valor<50950000:
        operacion=valor*0.015
    if valor>=50950000 and valor<114640000:
        operacion=valor*0.025
    if valor>=114640000:
        operacion=valor*0.
    operacionf=valor-operacion
    print("VALOR: ",valor)
    print("DESCUENTO APLICADO: ",operacion)
    print("TOTAL: ",operacionf)

alza()