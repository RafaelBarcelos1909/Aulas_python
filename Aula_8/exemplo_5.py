print("_*" * 20)
print("1- programador de sistemas:")
print("2 - analista de sistemas:")
print("3 - analista de banco de dados")
print("_*" * 20)
salario = float(input("digite o salario do colaborador: R$"))
cargo = int(input("digite o cargo do colaborador: R$"))

if cargo < 1 or cargo > 3 :
    print("cargo invalido")
elif cargo == 1:
    '''Acrescimo de 30% sobre o salario atual. Mesmo que:
       salario = salario * 1.3 ou
       salario = salario + salario * 0.3'''
    salario *= 1.3
    print(f'Novo salário: R$ {salario:.2f}')
elif cargo == 2:
    '''Acrescimo de 20% sobre o salario atual. Mesmo que:
       salario = salario * 1.2 ou
       salario = salario + salario * 0.2'''
    salario *= 1.2
    print(f'Novo salário: R$ {salario:.2f}')
else:
    '''Acrescimo de 15% sobre o salario atual. Mesmo que:
       salario = salario * 1.15 ou
       salario = salario + salario * 0.15'''
    salario *= 1.15
    print(f'Novo salário: R$ {salario:.2f}')