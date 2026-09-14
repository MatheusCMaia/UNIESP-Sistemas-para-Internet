nota1, nota2, nota3 = input("Digite as 3 notas com um espaço (Ex: 1 2 3): ").split()
nota1, nota2, nota3 = float(nota1), float(nota2), float(nota3)
media = (nota1 + nota2 + nota3) / 3
frequencia = int(input("Digite a frequencia do aluno sem a %: "))

print(f'''
Média do aluno: {media:.2f}
Frequência do aluno: {frequencia}%
''')
if media < 7 and frequencia < 75:
    print("Situação: Reprovado por falta de frequência e nota")
elif media >= 7 and frequencia < 75:
    print("Situação: Reprovado por falta de frequência")
elif media < 7 and frequencia >= 75:
    if media >= 4:
        print("Situação: Prova Final")
    else:
        print("Situação reprovado por nota")
else: 
    print("Situação: Aprovado por média e nota")