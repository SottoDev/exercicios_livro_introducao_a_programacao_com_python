salario = float(input("Digite o salario: "))

if salario > 1250:
    aumento = salario*0.1
    salario_novo = salario+aumento
    print(f"Seu aumento será de: R$ {salario_novo:7.2f}")
    

elif salario <= 1250:
    aumento = salario*0.15
    salario_novo = salario+aumento
    
    print(f"Seu aumento será de: R$ {salario_novo:7.2f}")