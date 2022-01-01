
num = input("Digite um número inteiro: ")
tam=len(num)
num=int(num)
i=1

digigual=False

while i<tam and not digigual:
    dig1=num%10
    num=num//10
    dig2=num%10
    i=i+1
    if dig1==dig2:
        digigual=True

if digigual:
    print("sim")
else:
    print("não")
