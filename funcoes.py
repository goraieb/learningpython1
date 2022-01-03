def soma (a,b,c):
    return a+b+c

def multiplica (a,b,c):
    return a*b*c

def nome_do_time ():
    return "Guilherme"

def quieta():
    x=30
    print("X é",x)


def fatorial(n):
    if n<0:
        valor=0
    else:
        valor = 1
        if n >= 0:
            while n>1:
                valor = valor * n
                n = n-1
    return valor

def numero_binomial(n,k):
    x=fatorial(n)
    y=fatorial(k)
    z=fatorial(n-k)
    return x/(y*z)


def testa_fatorial():
    funciona=True
    if fatorial(1)!=1:
        funciona=False
    else: print("funciona para 1")
    if fatorial(2)!=2:
        funciona=False
    else:
        print("funciona para 2")
    if fatorial(0)!=1:
        funciona=False
    else:
        print("funciona para 0")
    if fatorial(5) != 120:
        funciona=False
    else:
        print("funciona para 5")
    return print(funciona)




