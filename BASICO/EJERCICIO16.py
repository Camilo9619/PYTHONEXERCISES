def operacion():
    dias=int(input("Digite cantidad horas: "))
    gastos_ad=float()
    fondo=float()
    valor=float()
    valor=37000
    valorf=dias*valor
    valorarl=float()
    gastos_ad=valorf*0.05
    fondo=valorf*0.125
    valorarl=valorf*0.035
    print("DESCUENTOS LEY: ",gastos_ad)
    print("GASTOS ADMINISTRATIVOS: ",fondo)
    print("FONDO ADMINISTRATIVO: ",valorarl)
    return gastos_ad,fondo,valorarl


v=float()
v=operacion()



