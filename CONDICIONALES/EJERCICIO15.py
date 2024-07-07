def pcs():
    valor=float(input("Digite cantidad: "))
    precio=float()
    precio=985000
    operacion1=precio*valor
    operacion=float()
    desc=float()
    if valor<5:
        desc=0.1*operacion1
        operacion=operacion1-desc
    if valor>=5 and valor<10:
        desc=0.2*operacion1
        operacion=operacion1-desc
    if valor>10:
        desc=0.4*operacion1
        operacion=operacion1-desc
    print("CANTIDAD: ",valor)
    print("DESCUENTO: ",desc)
    print("PRECIO: ",operacion1)
    print("VALOR:",operacion)
pcs()
