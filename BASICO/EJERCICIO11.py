def cesantias():
    salario=int(input("Digite salario: "))
    dias=int(input("Digite dias trabajados:"))
    op=float()
    op=(salario*dias)/360
    op1=float()
    op1=(op*dias*0.12)/360
    print("Sueldo: ",salario)
    print("Su cesantia es: ",op)
    print("Su interes en cesantias es: ",op1)
    return op,op1


val=float()
val=cesantias()


        