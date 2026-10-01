zeroavintecinco = 0
vinteseisasessenta = 0
maisquesessenta = 0

while True:
    print('''
======================
Quer adicionar mais uma idade:

1 - Sim
2 - Não

======================
''')
    resposta = int(input("Digite sua resposta (1/2): "))
    if resposta == 1:
        idade = int(input("Digite a idade: "))
        if idade >= 0 and idade <= 25:
            zeroavintecinco += 1
        elif idade >= 26 and idade <= 60:
            vinteseisasessenta += 1
        else:
            maisquesessenta += 1
    elif resposta == 2:
        break
    else:
        print("Digite um valor válido!")

print(f"Idades de 0 a 25: {zeroavintecinco}")
print(f"Idade de 26 a 60: {vinteseisasessenta}")
print(f"Idade maior que 60: {maisquesessenta}")