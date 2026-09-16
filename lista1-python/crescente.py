numero1 , numero2, numero3 = input("Digite os números com espaço (Ex: 1 2 3): ").split()
numero1, numero2, numero3 = int(numero1), int(numero2), int(numero3)
numeros = []
numeros.append(numero1)
numeros.append(numero2)
numeros.append(numero3)
numeros.sort()
print("A ordem crescente é: ")
for i in numeros:
    print(i)


#Sem usar lista nem sort

print("------------------------")

if numero1 > numero2 and numero2 > numero3:
    print(numero3, numero2, numero1)
elif numero1 > numero3 and numero3 > numero2:
    print(numero2, numero3, numero1)
elif numero2 > numero1 and numero1 > numero3:
    print(numero3, numero1, numero2)
elif numero2 > numero3 and numero3 > numero1:
    print(numero1, numero3, numero2)
elif numero3 > numero1 and numero1 > numero2:
    print(numero2, numero1, numero3)
elif numero3 > numero2 and numero2 > numero1:
    print(numero1, numero2, numero3)
else:
    print("Todos são iguais")