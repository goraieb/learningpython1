num = input("Digite um número inteiro: ")
tam=len(num)
num=int(num)
i=1
valor=0

while i<tam:
    valor = valor + num%10
    num=num//10
    i=i+1

valor=valor+num
print(valor)
