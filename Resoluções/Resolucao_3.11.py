print("="*30)
print("Mercadinho da ZaZa")
print("="*30)
print("PROMOÇÃO DO DIA, COMPRAND0 3 CARTELAS DE OVO, VOCE GANHA 10% DE DESCONTO")

cartelas = int(input("Quantas cartelas voce vai querer?: "))
preco = 21

if cartelas >= 3:
    desconto = 10
    calculo = desconto/100
    pago_com_desconto = preco - desconto
    print(f"Valor pago R$ {pago_com_desconto:.2f}")
    
elif cartelas < 3:
    print(f"Valor pago R$ {preco:.2f}")