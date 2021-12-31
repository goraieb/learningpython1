import math

x1=float(input("Digite a coordenada x do primeiro ponto: "))
y1=float(input("Digite a coordenada y do primeiro ponto: "))

x2=float(input("Digite a coordenada x do segundo ponto: "))
y2=float(input("Digite a coordenada y do segundo ponto: "))

p1=(x1,y1)
p2=(x2,y2)

d = math.dist(p1,p2)

if d<10:
    print("perto")
else:
    print("longe")
