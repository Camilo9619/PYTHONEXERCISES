def operacion():
    val=float(input("Digite valor: "))
    op1=float()
    op2=float()
    op1=val/3600
    op2=val/60
    print("Horas: ",op1)
    print("Minutos: ",op2)
    print("Segundos: ",op2)
    return op1,op2

v=float()
v=operacion()


    