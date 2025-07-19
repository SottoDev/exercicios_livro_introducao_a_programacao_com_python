km_percorrido  = int(input("Quantos KMs voce percorreu?: "))
dias_alugado = int(input("Quantos dias pretendeficar com o carro alugado: "))
preço_dias = dias_alugado*60
preço_km = km_percorrido*0.15
preço_a_pagar = preço_dias+preço_km



print(f"O preço do aluguel é de R$ {preço_dias} e o da kilometragem é de R$ {preço_km}, somando os dois temos um preço total a ser pago é de R$ {preço_a_pagar}")