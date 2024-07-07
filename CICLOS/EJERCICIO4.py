def cliente():
    num=int(input("Digite cantidad: "))
    for i in range(num):
        nombre=input("Digite nombre: ")
        cantidad=int(input("Digite cantidad producto: "))
        if(cantidad>10):
            print("El producto es de 10% descuento")
        else:
            print("No hay descuento")

cliente()