valor1 = 30
valor2 = 20

if valor1 > valor2:
    print(f"valor 1 é maior pois {valor1} é maior que {valor2}")
elif valor1 != valor2:
    print(f"valor 2 é maior pois {valor2} é maior que {valor1}")
else:
    print(f"Os dois são iguais")

'''
===========================================================================================
'''

senha = str(input("Fale, amigo e entre: "))
if senha == "amigo":
    print("Acesso autorizado")
else:
    print("Acesso não autorizado")


'''
===========================================================================================
'''

if str(input("Fale, amigo e entre: ")).upper() == "AMIGO":
    print("Autorizado")
else:
    print("Negado")


'''
==============================================================================================
'''

nota1, nota2, nota3 = input("Digite as 3 notas: ").split()
nota1, nota2, nota3 = float(nota1), float(nota2), float(nota3)
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Aprovado")
elif media < 7 and media >= 4:
    print("Prova final")
else:
    print("Reprovado")


'''
==============================================================================================
'''


print('''
=============================================
            CALCULADORA
=============================================

[1] SOMA
[2] SUBTRAÇÃO
[3] MULTIPLICAÇÃO
[4] DIVISÃO
[5] NENHUM

=============================================
''')

opcao = input("Digite a opção da operação que deseja utilizar: ")
if opcao == '1':
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print(f"A soma de {valor1} + {valor2} é igual: {valor1+valor2}")
elif opcao == '2':
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print(f"A subtração do {valor1} menos {valor2} é igual: {valor1 - valor2}")
elif opcao == '3':
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print(f"A multiplicação do {valor1} com {valor2} é igual: {valor1 * valor2}")
elif opcao == '4':
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print(f"A divisão do {valor1} com {valor2} é igual: {valor1/valor2}")
elif opcao == '5':
    print("Até a próxima")
else:
    print("Digite uma opção válida da próxima vez!")

'''
===========================================================================
'''

nota1, nota2, nota3 = input("Digite as 3 notas com um espaço (Ex: 1 2 3): ").split()
nota1, nota2, nota3 = float(nota1), float(nota2), float(nota3)
media = (nota1 + nota2 + nota3) / 3
frequencia = int(input("Digite a frequencia do aluno sem a %: "))

print(f'''
Média do aluno: {media}
Frequência do aluno: {frequencia}
''')
if media < 7 and frequencia < 75:
    print("Situação: Reprovado por falta de frequência e nota")
elif media >= 7 and frequencia < 75:
    print("Situação: Reprovado por falta de frequência")
elif media < 7 and frequencia >= 75:
    print("Situação: Reprovado por nota")
elif media >= 7 and frequencia >= 75:
    print("Situação: Aprovado por média e nota")