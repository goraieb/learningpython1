num=float(input("Digite um número: "))

sobra2=num%3
sobra1=num%5

if sobra1 ==0 and sobra2 ==0:
    print("FizzBuzz")
else:
    print(num)
