'''
3o Escreva um código que exiba um menu para o usuário com duas opções (1 - continuar, 2 -
sair). Exiba o menu até que o usuário digite 2. Caso o usuário informe outro valor diferente de
1 e 2, retornar que o valor é inválido.
'''

while True:
    print('''
-------------------------
---------MENU------------
-------------------------
[1] - Continuar       
[2] - Sair            
-------------------------
''')
    entrada = int(input('Digite sua escolha: '))
    if entrada != 1 and entrada != 2:
        print("Digite um número válido!")
    elif entrada == 2:
        break
        
