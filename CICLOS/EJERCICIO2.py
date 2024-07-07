valor=int(input("Digite valor:" ))
operacion=float()
operacion=0
for i in range(0,valor):
    temp=float(input("Digite temperatura: "))
    operacion=operacion+temp/valor
print(operacion)

