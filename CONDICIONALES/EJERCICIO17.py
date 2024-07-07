def valor():
    num=float(input("Digite valor: "))
    pinos=float()
    cedro=float()
    oyamel=float()
    areaocp=float()
    areaoco=float()
    areaocc=float()
    cantidadp=float()
    cantidadoy=float()
    cantidadce=float()
    if num>1000000:
        pinos=num*0.7
        cedro=num*0.2
        oyamel=num*0.1
    else:
        pinos=num*0.5
        oyamel=num*0.3
        cedro=num*0.2
    areaocp=pinos/num
    areaoco=oyamel/num
    areaocc=cedro/num
    cantidadp=areaocp*8
    cantidadce=areaocc*10
    cantidadoy=areaoco*15
    print("PINOS: ",cantidadce)
    print("OYAMEL: ",cantidadoy)
    print("CEDRO: ",cantidadp)
valor()
    
    
