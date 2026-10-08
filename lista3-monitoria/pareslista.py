'''
8o Dada a lista valores=[1, 2, 3, 4, 5, 6, 7, 8], crie uma lista apenas com os valores pares
'''

#vamos criar a lista pedida
lista = [1,2,3,4,5,6,7,8]

#vamosr criar uma lista vazia
lista_pares = []

#iremos usar o for novamente para percorrer a lista
for i in lista:
    #o i novamente terá os valores dos elementos da lista
    #primeira repetição terá valor 1, na segunda valor 2 e assim até o fim da lista
    #vamos colocar uma condição para verificar se o elemento "i" é par ou não
    if i%2 == 0:
        #Está condição verifica se i é par ou não, caso você não entenda como funciona veja o vídeo que postei ontem
        lista_pares.append(i)

print(lista_pares)