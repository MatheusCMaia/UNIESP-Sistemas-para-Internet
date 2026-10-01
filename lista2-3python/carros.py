carros = ["Fiat","Chevrolet","Ford","Honda"]

carros.insert(1,"Jeep")
carros.pop(len(carros) - 1)
carros.append("Toyota")
print(f"Existe {len(carros)} na lista")
carros.sort()
print(carros)