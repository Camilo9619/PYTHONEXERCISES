def valor():
    num=float(input("Digite valor: "))
    operacion=float()
    total=float()
    if num>1000000:
        print("INTERES 5%")
        operacion=num*0.05
        total=num-operacion
    if num>750000 and num<=1000000:
        print("INTERES 3.85%")
        operacion=num*0.0385
        total=num-operacion
    if num>500000 and num<=750000:
        print("INTERES 2.5%")
        operacion=num*0.025
        total=num-operacion
    if num<500000:
        print("INTERES 1.75%")
        operacion=num*0.0175
        total=num-operacion
    print("VALOR PRESTAMO: ",total)
valor()