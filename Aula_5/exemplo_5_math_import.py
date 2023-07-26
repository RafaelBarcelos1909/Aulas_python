#efetuando o import da classe matematica

from math import sqrt
print('dados do p1: ')
x1 = float(input("digite x1:"))
y2 = float(input("digite y1:"))
print("dados do p2: ")
x2 = float(input("digite x2:"))
y2 = float(input("digite y2:"))

d = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

print(f"A distacia entre p1 e p2 = {d:.2f}")