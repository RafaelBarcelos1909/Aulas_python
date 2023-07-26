sobrenome = input('informe o sobre nome de um(a) apresentador ')

if sobrenome.upper() == 'PINHEIRO' or sobrenome.upper() == 'ARAÚJO':
    print('Bom dia Nação!')
elif sobrenome.upper() == 'BONNER' or sobrenome.upper() == 'VASCONCELLOS':
    print('Jornal Brasileiro!')
else:
    print("apresentador desconhecido (a).")
