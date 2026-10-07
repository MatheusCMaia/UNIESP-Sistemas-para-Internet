'''
5o) Escreva um código que receba 6 valores do usuário, exiba a sua soma e a sua média. Fazer
usando laços de repetição.
'''

soma = 0
for i in range(6):
    valor = int(input("Digite um valor: "))
    soma = soma + valor

print(f"A soma dos valores é: {soma}")
print(f"A média dos valores é: {soma/6:.2f}")
