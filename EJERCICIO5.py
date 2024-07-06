def suma():
    print("SUMA")
    a=int(input("Digite a: "))
    b=int(input("Digite b: "))
    suma=int()
    suma=a+b
    return suma
def resta():
    print("RESTA")
    a=int(input("Digite a: "))
    b=int(input("Digite b: "))
    resta=int()
    resta=a-b
    return resta
def multiplicacion():
    print("MULTIPLICACION")
    a=int(input("Digite a: "))
    b=int(input("Digite b: "))
    multiplicacion=int()
    multiplicacion=a*b
    return multiplicacion
def division():
    print("DIVISION")
    a=int(input("Digite a: "))
    b=int(input("Digite b: "))
    division=int()
    division=a/b
    return division
def potenciacion():
    print("POTENCIACION")
    a=int(input("Digite a: "))
    b=int(input("Digite b: "))
    potenciacion=int()
    potenciacion=pow(a,b)
    return potenciacion
def modulo():
    print("MODULO")
    a=int(input("Digite a: "))
    b=int(input("Digite b: "))
    modulo=int()
    modulo=a%b
    return modulo


v1=int()
v2=int()
v3=int()
v4=int()
v5=int()
v6=int()
v1=suma()
v2=resta()
v3=multiplicacion()
v4=division()
v5=potenciacion()
v6=modulo()
print("SUMA= ",v1)
print("RESTA= ",v2)
print("MULTIPLICACION= ",v3)
print("DIVISION= ",v4)
print("POTENCIACION= ",v5)
print("RESIDUO= ",v6)
