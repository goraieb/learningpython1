import math

x1=float(input("Digite a coordenada x do primeiro ponto: "))
y1=float(input("Digite a coordenada y do primeiro ponto: "))

x2=float(input("Digite a coordenada x do segundo ponto: "))
y2=float(input("Digite a coordenada y do segundo ponto: "))

d2 = (x1-x2)**2 + (y1-y2)**2
d=math.sqrt(d2)


print(d)

if d<10:
    print("perto")
else:
    print("longe")
