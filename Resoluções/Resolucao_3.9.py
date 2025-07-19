    
dias = int(input("Digite o dia: "))
horas = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segungos: "))

data_e_hora = (f"Dia {dias}, as {horas}:{minutos}:{segundos}")

# dia_em_segundos = dias*86400 
# # 1 dia = 24 horas | 1 hora = 60 minutos | 1 minutos = 60 segundos | 1d = 24x60x60 =86400 segundos 
# horas_em_segundos = horas*3600 
# # 1 hora = 60 minutos | 1 minutos = 60 segundos | 1hr = 60x60 = 3600 segundos
# minutos_em_segunds = segundos*60 
# #1 minutos = 60 segundos
# segundos_em_segundos = segundos
#1 segundo = 1 segundo

calculo_em_segundos = (dias*86400) + (horas*3600) + (minutos*60) + segundos

print(f" A date de {data_e_hora} convetida em segundos, são {calculo_em_segundos} segundos")