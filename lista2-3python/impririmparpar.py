numer1 = int(input("Digite o número: "))


if numer1%2 == 0:
    for i in range(0,numer1+1,2):
        print(i)
else:
    for i in range(1,numer1+1,2):
        print(i)
    