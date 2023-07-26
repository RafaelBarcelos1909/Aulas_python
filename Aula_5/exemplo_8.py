sal_minimo = float(input("informe o valor do salario minimo atual (R$):"))
sal_usuario = float(input("informe o valor do seu salario mensal (R$):"))
qtd_salarios = sal_usuario / sal_minimo

print(f"você recebe aproximadamente {qtd_salarios: .2f} salario(s) minimo(s)")
