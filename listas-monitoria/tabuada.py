'''
6o) Escreva um código que receba um valor inteiro de 0 a 10. Exiba a tabuada de 0 a 10 do valor
informado.
'''

valor = int(input("Digite um valor: "))

for i in range(0,11):
    print(f"{valor} x {i} = {valor * i}")