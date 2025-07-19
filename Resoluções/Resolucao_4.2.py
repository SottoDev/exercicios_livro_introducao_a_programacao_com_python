import random

velocidade = random.randint(10, 100)

if velocidade < 80:
    print(f"Voce está a {velocidade} numa via de 80km/h")


elif velocidade >= 80:
    km_alem_do_limite = velocidade-80
    multa= km_alem_do_limite*5
    print(f"Voce estava a {velocidade}KM/h em uma via de 80Km/h. A multa de R$ {multa} sera entregue na sua residencia")