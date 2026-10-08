'''
5o Tendo a lista números=[2, 4, 6, 8], retorne uma lista com o quadrado de cada um desses
valores
'''
#A lista inicial pedida
lista_numeros = [2,4,6,8]
#Agora a questão pede para retornar uma lista com o quadrado de cada um desses valores
#Eu irei usar o for para resolver essa questão
#Antes de criar o for irei fazer uma lista agora vazia onde irei adicionar esses valores
lista_quadrados = []
for i in lista_numeros:
    #O for ele pode ser usado para percorrer listas diretamente onde o i receberá os valores dos elementos
    #Nesse caso por exemplo, o i na primeira repetição terá o valor 2, na segunda repetição 4 e assim sucessivamente
    #Então irei dar append na lista vazia e o valor será i * i que será seu quadrado
    lista_quadrados.append(i*i)

print(lista_quadrados)