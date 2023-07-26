sal_base = 1500
comissao = 200

corretor = input('digite o nome do corretor:')
qtd_vendas = int(input("informe a quantidade de imoveis vendidos:"))
qtd_vendas = float(input("informe o valor total de vendas do corretor (R$): "))

sal_final = sal_base + comissao * qtd_vendas + qtd_vendas * 0.05

print(f'o salario final do {corretor} é de R${sal_final:.2f}')
