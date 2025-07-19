qnt_cigarros = int(input("Quantos cigarros voce fuma por dia? "))
tempo_gasto = qnt_cigarros * 10


if qnt_cigarros < 6: #minutos
    tempo_de_vida_seg = tempo_gasto*1
    seg_em_dias = tempo_de_vida_seg/1440
    print(f"Fumando {qnt_cigarros} cigarros por dia, voce perde {tempo_gasto} minutos da sua vida, que da um total {seg_em_dias:.2f} dias")

elif qnt_cigarros < 60: #horas
    tempo_de_vida_horas= tempo_gasto/60
    horas_em_dias = tempo_de_vida_horas/1440
    print(f"Fumando {qnt_cigarros} cigarros por dia, voce perde {tempo_gasto} horas da sua vida, que da um total {horas_em_dias:.2f} dias")
    
elif qnt_cigarros >=61: # dias
    tempo_de_vida = tempo_gasto/1440
    print(f"Fumando {qnt_cigarros}  cigarros por dia, voce perde {tempo_gasto:.2f} dias da sua vida")
    