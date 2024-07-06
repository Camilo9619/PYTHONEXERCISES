def cuadrante():
    valor=int(input("Digite valor: "))
    if valor>0 and valor<=90:
        print("PRIMER CUADRANTE")
    if valor>90 and valor<=180:
        print("SEGUNDO CUADRANTE")
    if valor>180 and valor<=270:
        print("TERCER CUADRANTE")
    if valor>270 and valor<=360:
        print("CUARTO CUADRANTE")
cuadrante()