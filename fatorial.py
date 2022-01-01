
num = int(input("Digite um número natural: "))

valor = 1

if num >= 0:
    while num>1:
        valor = valor* num
        num=num-1

    print(valor)
else:
    print("O número digitado não é um número natural (>=0).")
