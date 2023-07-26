
quantidade = int(input("numero de camisas"))
valor = 78.90
total = quantidade * valor
if quantidade < 5:
    total = total * (1 -3/100)
elif quantidade < 10:
    total = total * (1 -5/100)
else:
    total = total * (1-7/100)
print(f"valor final : R$ {total:.2f}")
