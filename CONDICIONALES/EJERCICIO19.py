def operacion():
    a=float(input("Digite valor: "))
    b=float(input("Digite valor: "))
    c=float(input("Digite valor: "))
    operacion=(pow(b,2))-4*a*c
    if operacion<0:
        print("OPERACION: ",operacion)
        print("La ecuacion no tiene solucion real")
    if operacion>0:
        print("OPERACION: ",operacion)
        print("La ecuacion tiene dos soluciones")
    if operacion==0:
        print("OPERACION: ",operacion)
        print("La ecuacion tiene una solucion")
operacion()