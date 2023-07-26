quantidade = float(input("digite a quantidadede camisas: "))
valor = 78.50
total = quantidade * valor

if quantidade <= 5:
    total = total * (1 - 3/100)
else:
    if quantidade < 10:
        total = total * (1 - 5/100)
    else:

        total = total * (1 - 7/100)

print(f"valor total é {total:.2f}")
