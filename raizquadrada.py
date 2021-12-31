import math

a=float(input("Digite o valor de a: "))
b=float(input("Digite o valor de b: "))
c=float(input("Digite o valor de c: "))

d = b**2 - 4*a*c
    
if a ==0:
    print("a raiz da equação é",-c/b)

else:    
    if d<0:
        print("esta equação não possui raízes reais")


    else:
        raiz1=(-b+math.sqrt(d))/(2*a)
        raiz2=(-b-math.sqrt(d))/(2*a)

        if d==0:
            print("a raiz desta equação é",raiz1)

        if d>0:
            print("as raizes da equação são", raiz1, "e", raiz2)

