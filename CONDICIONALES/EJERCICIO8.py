def nota():
    valor=float(input("Digite valor: "))
    op1=valor*0.15
    op2=valor*0.3
    op3=valor*0.25
    op4=valor*0.1
    op5=valor*0.2
    opfinal=op1+op2+op3+op4+op5
    if opfinal>=3.3:
        print("Aprobado")
    else:
        print("Paila")

nota()