def imc():
    peso=float(input("Digite peso: "))
    altura=float(input("Digite altura: "))
    imc=peso/(altura**2)
    print("Su IMC es: ",imc)
    return imc
v=float()
v=imc()