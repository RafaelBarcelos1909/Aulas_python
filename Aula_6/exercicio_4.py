alt1 = float(input("digite a altura da primeira pessoa(em metros):"))

alt2 = float(input("digite a altura da segunda pessoa(em metros):"))

alt3 = float(input("digite a altura da tercerira pessoa (em metros):"))

mais_alto = alt1
est_med = alt1
mais_baixa = alt1

if alt1 > alt2 and alt1 > alt3:
    mais_alto = alt1
    if alt2 > alt3:
        est_med = alt2
        mais_baixa = alt3
    else:
        est_med = alt3
        mais_baixa = alt2

elif alt2 > alt1 and alt2 > alt3:
    mais_alto = alt2
    if alt1 > alt3:
        est_med = alt1
        mais_baixa = alt3

    else: 
        est_med = alt3
        mais_baixa = alt1
else:
    mais_alto = alt3

    if alt1 > alt2:
        est_med = alt1
        mais_baixa = alt2
    else:
        est_med = alt2
        mais_baixa = alt1
print(f'\n{mais_baixa}m,{est_med}m e {mais_alto}m')


