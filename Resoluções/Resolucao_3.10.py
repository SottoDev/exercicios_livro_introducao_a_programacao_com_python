print("="*30)
print("Quanto o seu salario subiu?")
print("="*30)

salario_antigo = int(input("Qual é o seu salario antes do reajuste?: "))
porcentagem = int(input("o ajuste foi de quantos porcento?(Digite apenas numeros): "))
salario_novo = salario_antigo + (porcentagem/100)
total_do_aumento = salario_novo - salario_antigo

print(f"O seu salario foi aumentado em {total_do_aumento:.2f}.Voce receverá R$ {salario_novo:.2f}")