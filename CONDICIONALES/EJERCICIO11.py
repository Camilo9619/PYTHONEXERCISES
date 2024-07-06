def imc():
    peso=float(input("Digite peso: "))
    altura=float(input("Digite altura: "))
    imc= peso/(altura**2)
    if imc<16:
        print("Delgadez grave")
    if imc>=16 and imc<=16.99:
        print("Delgadez moderada")
    if imc>=17 and imc<=18.49:
        print("Delgadez leve")
    if imc>=18.5 and imc<=24.99:
        print("Peso normal")
    if imc>=25 and imc<=29.99:
        print("Sobrepeso")
    if imc>=30 and imc<=34.99:
        print("Obesidad Tipo 1")
    if imc>=35 and imc<=39.99:
        print("Obesidad Tipo 2")
    if imc>=40 and imc<=49.99:
        print("Obesidad Tipo 3(obesidad morbida)")
    if imc>=50:
        print("Obesidad tipo 4 o extrema")
imc()