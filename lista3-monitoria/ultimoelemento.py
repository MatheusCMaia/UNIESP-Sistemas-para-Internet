'''2o Tendo a lista lista=[2, 4, 6, 8, 10, 12, 14], acesse o último elemento da lista, mas
subentenda que você não sabe qual o tamanho dessa lista.'''

lista = [2,4,6,8,10,12,14]
#Descobrir o ultimo indice da lista
ultimoindice = len(lista) - 1
#O indice sempre será a posição menos 1, a função len ela pega o tamanho da lista, por exemplo
#Se temos a lista criada com 7 elementos, o ultimo elemento tem a posição 7, o seu indice será 6 pois 7-1 = 6
print(lista[ultimoindice])
#Neste print estamos printando apenas o ultimo elemento sem saber o tamanho da lista