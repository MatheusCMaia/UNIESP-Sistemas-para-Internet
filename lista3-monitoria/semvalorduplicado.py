'''
7o Tendo a lista valores=[1, 1, 2, 2, 3, 4, 8, 9, 9], crie uma lista sem que os valores
apareçam duplicados
'''

#Vamos criar a lista inicial
lista_valores = [1,1,2,2,3,4,8,9,9]
#A questão pede para criar uma lista sem que os valores se repitam
#Vamos criar uma lista vazia
lista_sem_duplicacoes = []
#Agora vamos usar um for novamente
for i in lista_valores:
    #Este for ele vai percorrer a lista_valores e o i terá os valores da lista em cada repetição
    #Na primeira repetição terá valor 1, na segunda 1, na terciera 2, na quarta 2 até o fim da lista
    #Nós iremos colocar uma "verificação" para garantir que não tenha valores duplicados
    if i not in lista_sem_duplicacoes:
        #Esta condição verifica se i não está dentro de lista_sem_duplicações
        #Caso o valor já esteja ele não irá adicionar
        lista_sem_duplicacoes.append(i)
print(lista_sem_duplicacoes)