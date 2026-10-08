'''
3o Tendo a lista lista=[5, 10, 15, 20], adicione de uma única vez os valores [25, 30, 35,
40] ao final da lista
'''
#Aqui criamos a lista que foi pedida
lista = [5,10,15,20]
#Aqui criamos a segunda lista com os valores ditos na questão
lista2 = [25,30,35,40]
#A questão pede para adicionarmos a lista2 no final da lista1
#A função que adiciona uma lista ao final da outra é o extend
#Aqui estamos adicionando ao final da lista1 os elementos da lista2
lista.extend(lista2)
print(lista)