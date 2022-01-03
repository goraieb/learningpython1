valor1=input("Digite um número inteiro maior que zero: ")
d = input("Digite o dígito que está buscando: ")
count=0

for x in valor1:
    if x == d:
        count=count+1


print("O número",d, "aparece", count,"vezes em",valor1)
