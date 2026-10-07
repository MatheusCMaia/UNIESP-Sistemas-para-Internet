'''
2o Escreva um código que receba um valor inteiro e caso o valor informado seja par, imprimir
os valores pares de zero até o valor informado, caso seja ímpar, informar os valores ímpares de
1 ao valor informado.
'''

valor = int(input("Digite um valor: "))

if valor%2 == 0:
    for i in range(0,valor+1,2):
        print(i)
else:
    for i in range(1,valor+1,2):
        print(i)