'''
Escreva um programa que receba a idade de n pessoas e ao final informe a quantidade de
pessoas com idade entre 0 e 25 anos, 26 e 60 anos e maior que 60 anos. Continue recebendo
idades até que o usuário informe que não quer mais receber idades.
'''

zeroavintecinco = 0
vinteseisasessenta = 0
maisquesessenta = 0

while True:
    print('''
===================
Digite uma opção:

[1] - Adicionar
[2] - Parar

===================
''')
    opcao = int(input("Digite sua escolha: "))
    if opcao != 1 and opcao != 2:
        print("Digite um valor válido")
    elif opcao == 2:
        break
    else:
        idade = int(input("Digite a idade que você deseja adicionar: "))
        if idade >= 0 and idade <= 25:
            zeroavintecinco = zeroavintecinco + 1 
        elif idade > 25 and idade <= 60:
            vinteseisasessenta = vinteseisasessenta + 1
        elif idade > 60:
            maisquesessenta = maisquesessenta + 1


print(f"Tem {zeroavintecinco} pessoas entre 0 a 25 anos")
print(f"Tem {vinteseisasessenta} pessoas entre 26 a 60 anos")
print(f"Tem {maisquesessenta} pessoas acima de 60 anos")
