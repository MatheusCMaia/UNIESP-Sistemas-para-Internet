acabar = 1
while acabar == 1:
    print('''
=============================
MENU
=============================

1 - Continuar
2 - Sair

''')
    valor = input("Digite o que você deseja fazer: ")
    if valor == 2:
        print("Programa encerrado!")
        acabar = 0
    elif valor != 1:
        print("Digite um valor válido!")