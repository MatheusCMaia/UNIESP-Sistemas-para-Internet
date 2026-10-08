'''
6o Dada a lista valores=[10, 20, 30, 40, 50], remova os valores maiores que 30 com apenas
um comando
'''
#A lista pedida na questão
valores = [10,20,30,40,50]
#Essa resolução por se tratar de apenas um comando será mais dificil de entender mas tentarei explicar da melhor forma
valores = [x for x in valores if x <= 30]
#A lista terá valores x, onde esse x irá percorrer a própria lista, o IF está verificando se o valor que x terá
#É menor ou igual a 30, ou seja por se tratar de um for ele irá percorrer e terá os valores 10,20,30,40,50
#O if está garantindo que a lista terá apenas valores menores igual a 30

