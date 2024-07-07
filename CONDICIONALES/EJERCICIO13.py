def salario():
    valor=float(input("Digite valor: "))
    ri=float(input("Digite valor riesgo: "))
    salud=valor*0.125
    pension=valor*0.16
    operacionriesgo=float()
    riesgo=float()
    if ri==1:
        operacionriesgo=valor*0.00522
        riesgo=valor-operacionriesgo
    if ri==2:
        operacionriesgo=valor*0.01044
        riesgo=valor-operacionriesgo
    if ri==3:
        operacionriesgo=valor*0.02436
        riesgo=valor-operacionriesgo
    if ri==4:
        operacionriesgo=valor*0.04350
        riesgo=valor-operacionriesgo
    if ri==5:
        operacionriesgo=valor*0.0696
        riesgo=valor-operacionriesgo
    print("VALOR: ",valor)
    print("RIESGO: ",ri)
    print("SALUD: ",salud)
    print("PENSION: ",pension)
    print("OPERACION RIESGO: ",operacionriesgo)
    print("VALOR RIESGO: ",riesgo)

salario()
    
    




