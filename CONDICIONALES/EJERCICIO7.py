def bisies():
    v=int(input("Digite valor: "))
    if v%4==0 and v%100!=100 or v%400==0:
        print("Bisiesto")
    else:
        print("No es bisiesto")

bisies()