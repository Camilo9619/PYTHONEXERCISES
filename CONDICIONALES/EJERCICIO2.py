def numdesc():
    a=float(input("Digite numero: "))    
    b=float(input("Digite numero: "))
    c=float(input("Digite numero: "))
    if a<b<c:
        print(a,b,c)
    if(b<c<a):
        print(b,c,a)
    if(c<b<a):
        print(c,b,a)
    
numdesc()