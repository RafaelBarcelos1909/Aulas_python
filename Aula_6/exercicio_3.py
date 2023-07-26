from math import sqrt
# coordenadas X e Y do ponto 1
x1 = float(input("digite a coordenada X do ponto 1 "))
y1 = float(input("digite a coordenada Y do ponto 1"))

# coordenadas X e Y do ponto 2
x2 = float(input("\ndigite a coordenada X do ponto 2"))
y2 = float(input("digite a coordenada Y do ponto 2"))

# coordenadas X e Y do ponto 3
x3 = float(input("\ndigite a coordenada X do ponto 3"))
y3 = float(input("digite a coordenada Y do ponto 3"))
# calculo dos lados dos triangulos
L1 = sqrt((x2 - x1)**2 + (y2 - y1)**2)  # distancia entre p1 e p2
L2 = sqrt((x3 - x1)**2 + (y3 - y1)**2)  # distancia entre p1 e p3
L3 = sqrt((x3 - x2)**2 + (y3 - y2)**2)  # distancia entre p2 e p3
# considerando que as três condições de existência sejam verdadeiras
cond1 = True
cond2 = True
cond3 = True
# verifica se algum lado é igual a zero

if L1 == 0 or L2 == 0 or L3 == 0:
    cond1 = False
# verifica se algum lado é maior que a soma dos outros dois
if L1 <= (L2+L3) or L2 > (L1 + L3) or L3 > (L1+L2):
    cond2 = False
# Verificar algum lado não é maior que o módulo da diferença entre os outros ?
if L1 <= abs(L2 - L3) or L2 <= abs(L1 - L3) or L3 <= abs(L1 - L2):
    cond3 = False
triangulo = True  # inicialmente, considere a existencia do tringulo
# Alguma condição de inexistencia foi identificada?
if cond1 == False or cond2 == False or cond3 == False:
    triangulo = False  # triangulo inexistente
    print("\nNenhum tringulo formado.\nMotivo(s):")
    if cond1 == False:
        print("pelo menos um lado é igual a zero.")
    if cond2 == False:
        print("pelo menos um dos lados é maior que a soma dos outros dois.")
    if cond3 == False:
        print("um dos lados é menor ou igual ao modulo da diferença.")
# triangulo existente
elif L1 == L2 == L3:
    print("\nTringulo Equilátero!")
elif L1 != L2 and L1 != L3 and L2 != L3:
    print("O triangulo é Escaleno.")
else:
    print("\nO triangulo é Isósceles.")

# todas condições de existencia do triangulo foram satisfeitas
if triangulo:
    print(f"Medida do lado 1: {L1:.2f}")
    print(f"Medida do lado 2: {L2:.2f}")
    print(f"Medida do lado 3: {L3:.2f}")
