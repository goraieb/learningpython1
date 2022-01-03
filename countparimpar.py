#! /usr/bin/env python3

entrada=input("Digite os valores da lista")

itens=entrada.split()

vetor = list(map(int, itens))

par=0
impar=0

for n in vetor:
    if n%2==1:
        impar=impar+1
    else:
        par=par+1



print(vetor)
print("par", par)
print("impar",impar)
