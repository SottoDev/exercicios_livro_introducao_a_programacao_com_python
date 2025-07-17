total_de_materias = 3
materia1 = 10
materia2 = 5
materia3 = 5
soma_notas = (materia1+materia2+materia3)
media = (soma_notas/total_de_materias)
corte = 7

if media < 7:
    print(f"O aluno foi reprovado com nota {media:.1f} de media ")
    # :.1f serve para ter apenas uma casa apos o . Ex: 1.20

elif media >= 7:
    print(f"O aluno foi aprovado com nota {media:.1f} de media") 
    # o f antes das aspas se chama F-String, é uma mandeira mais simples de colocar os dados no meio de um print.