n=input("Digite a n notas que os alunos tiveram. (valores inteiros de 0 a 10")
count=0
soma=0

for x in n:
    if x != " ":
        count=count+1
        soma=soma+int(x)

print("De um total de", count,"notas, a média é de,", soma/count)
