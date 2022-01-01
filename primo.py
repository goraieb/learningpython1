num0 = int(input("Digite um número natural: "))

num=num0-1

ehprimo=True

while num>1 and ehprimo:
    if num0 % num ==0:
        ehprimo=False
    num=num-1

if ehprimo == True:
    print("primo")
else:
    print("não primo")
