final = int(input("Digite até onde você deseja que seja mostrado: "))


termo1 = 0
termo2 = 1
termo3 = 1
print(termo1)
print(termo2)
while termo3 <= final:
    print(termo3)
    termo1 = termo2
    termo2 = termo3
    termo3 = termo2 + termo1
    

