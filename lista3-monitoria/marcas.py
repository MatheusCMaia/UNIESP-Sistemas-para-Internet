'''
4o Sendo a lista carros=[‘Fiat’, ‘Chevrolet’, ‘Ford’, ‘Honda’]
Adicione a marca Jeep na segunda posição da lista
Apague o último registro da lista
Adicione a marca Toyota a última posição da lista
Mostre quantos elementos possui a lista
Ordene a lista
'''

#Lista inicial criada
lista_carros = ['Fiat', 'Chevrolet', 'Ford', 'Honda']
#Adicionar a marca jeep na segunda posição da lista
lista_carros.insert(1,'Jeep')
#O insert funciona da seguinte maneira(indice, elemento)
#Como a questão pede na segunda posição colocamos o índice 1 pois, posição - 1 = índice
#Como a questão pede a segunda posição substituimos: 2 - 1 = 1
#A questão agora pede para apagar o último registro da lista
lista_carros.pop()
#O pop quando 
print(lista_carros)