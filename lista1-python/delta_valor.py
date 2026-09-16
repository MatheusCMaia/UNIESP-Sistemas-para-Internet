a,b,c = input("Digite os valores de a,b e c com espaço(Ex: 1 2 3)").split()
delta = ((int(b)) ** 2) - (4 * int(a) * int(c))
print(delta)
if delta < 0:
    print("Equação não possui valores reais")
else:
    x1 = ((int(b) * -1) + (delta ** (1/2))) / (2 * int(a))
    x2 = (-int(b) - (delta ** (1/2))) / (2 * int(a))
    print(f"x1 é igual: {x1:.2f}")
    print(f"x2 é igual: {x2:.2f}")