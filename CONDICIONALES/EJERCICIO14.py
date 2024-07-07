def operacion():
    valorv=float(input("Digite valor: "))
    valorf=float(input("Digite valor: "))
    operacion=float()
    operacion=valorv/valorf
    if(operacion<=3 and operacion>30):
        print("Frecuencias muy bajas")
    if(operacion>=30 and operacion<300):
        print("Frecuencias  bajas")
    if(operacion>=300 and operacion<3000):
        print("Frecuencias medias")
    if(operacion>=3000 and operacion<30000):
        print("Frecuencias altas ")
    if(operacion>=30000 and operacion<300000):
        print("Frecuencias muy altas ")
    if(operacion>=300000 and operacion<3000000):
        print("Frecuencias ultra altas")
    if(operacion>=3000000 and operacion<30000000):
        print("Frecuencias super altas")
    if(operacion>=30000000 and operacion<300000000):
        print("Frecuencias extra altas")
    print("VALOR= ",operacion)    

    
