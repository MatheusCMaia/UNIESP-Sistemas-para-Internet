'''
1o Escreva um código que receba 2 valores do tipo inteiro, faça sua soma e informe se o
resultado é par ou ímpar.
'''

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

soma = valor1 + valor2

if soma%2 == 0:
    print(f"O número {soma} é par!")
else:
    print(f"O número {soma} é ímpar")

