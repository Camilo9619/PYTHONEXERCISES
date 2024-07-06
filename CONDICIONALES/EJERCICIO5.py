
nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

if nombre1[0].lower() == nombre2[0].lower() or nombre1[-1].lower() == nombre2[-1].lower():
    print("Coincidencia")
else:
    print("No hay coincidencia")
