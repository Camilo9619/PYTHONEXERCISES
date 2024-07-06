
letra = input("Ingrese una letra: ")

if len(letra) != 1:
    print("No se puede procesar")
else:

    if letra.lower() in 'aeiou':
        print("Es Vocal")
    else:
        print("No es Vocal")
