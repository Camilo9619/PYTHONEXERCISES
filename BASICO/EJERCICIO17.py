def Resistencias():
    r1=float()
    r2=float()
    r3=float()
    r1=input("Digite r1: ")
    r2=input("Digite r2: ")
    r3=input("Digite r3: ")
    v1=float()
    v2=float()
    v3=float()
    v1=1/r1
    v2=1/r2
    v3=1/r3
    r=float()
    r=1/((v1)+(v2)+(v3))
    return r


f=float()
f=Resistencias()

