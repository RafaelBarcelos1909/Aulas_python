
print("calculo de grandezas elétricas")
print("################################")
print(" 1. tensao (em volt)")
print(" 2. resistencia (ohm)")
print(" 3. corrente (ampére)")
print("\n\n")
opcao = int(input("qual grandeza deseja calcular"))

if opcao < 1 or opcao > 3:
    print("opção invalida")

elif opcao == 1:
    R = float(input(" digite o valor da resistencia( em ohm):"))
    I = float(input("digite o valor da corrente(ampére): "))
    U = R * i

    print(f'\nU = {U:.2f}')
elif opcao == 2:
    U = float(input(" digite o valor da tensão (volt):"))
    I = float(input("digite o valor da corrente(ampére): "))
    R = U / I
    print(f'\nR = {R:.2f}')
else:
    U = float(input(" digite o valor da tensão (volt):"))
    R = float(input(" digite o valor da resistencia( em ohm):"))
    I = U / R
    print(f'\nI = {I:.2f}')
