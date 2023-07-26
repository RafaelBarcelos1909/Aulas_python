from math import sqrt
num1 = int(input("digite o primeiro numero"))

num2 = int(input("digite o segundo numero"))

cubo = pow(num2, 3)
media_geo = sqrt(num1 * num2)

print(f"\no cubo de {num2} é {cubo}")
print(f" a media geometrica entre {num1} e {num2} é {media_geo: .2f}")
