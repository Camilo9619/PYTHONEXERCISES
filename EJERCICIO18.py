def Balance():
    Salario=float(input("Digite valor: "))
    valor_alimentos=float()
    valor_libros=float()
    valor_boletos=float()
    valor_pasajes=float()
    valor_restante=float()
    valor_subtotal=float()
    valor_alimentos=Salario*0.2
    valor_libros=Salario*0.15
    valor_boletos=Salario*0.1
    valor_pasajes=Salario*0.15
    valor_subtotal=(valor_alimentos+valor_libros+valor_boletos+valor_pasajes)
    valor_restante=Salario-valor_subtotal
    print("SALARIO: ",Salario)
    print("VALOR ALIMENTOS: ",valor_alimentos)
    print("VALOR LIBROS: ",valor_libros)
    print("VALOR PASAJES: ",valor_pasajes)
    print("VALOR BOLETOS: ",valor_boletos)
    print("VALOR RESTANTE: ",valor_restante)
    return valor_restante

f=float()
f=Balance()