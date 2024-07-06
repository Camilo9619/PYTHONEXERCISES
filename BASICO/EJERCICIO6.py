import math

def TrianguloRectangulo():
    print("TrianguloRectangulo")
    a=float(input("Digite lado 1: "))
    b=float(input("Digite lado 2: "))
    c=float(input("Digite lado 3: "))
    area=float()
    perimetro=float()
    area=(a*b)/2
    perimetro=a+b+c
    print("AREA= ",area)
    print("PERIMETRO= ",perimetro)
    return area,perimetro
def Rectangulo():
    print("Rectangulo")
    a=float(input("Digite lado 1: "))
    b=float(input("Digite lado 2: "))
    area=float()
    perimetro=float()
    area=(a*b)
    perimetro=a+b
    print("AREA= ",area)
    print("PERIMETRO= ",perimetro)
    return area,perimetro
def Circulo():
    print("Circulo")
    a=float(input("Digite radio: "))
    area=float()
    area=(pow(a,2))*3.1415
    perimetro=float()
    perimetro=2*3.1415*a
    print("AREA= ",area)
    print("PERIMETRO= ",perimetro)
    return area,perimetro
def Cuadrado():
    print("Cuadrado")
    a=float(input("Digite lado: "))
    area=float()
    area=pow(a,2)
    perimetro=4*a
    print("AREA= ",area)
    print("PERIMETRO= ",perimetro)
    return area,perimetro
def TrianguloEquilatero():
    print("TrianguloEquilatero")
    a=float(input("Digite lado: "))
    area=float()
    area=(pow(a,2))*(pow(3,0.5))/4
    print("AREA= ",area)
    return area

v1=float()
v2=float()
v3=float()
v4=float()
v5=float()
v1=TrianguloRectangulo()
v2=Rectangulo()
v3=Circulo()
v4=Cuadrado()
v5=TrianguloEquilatero()


