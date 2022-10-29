a = [i for i in range(1,11)]
b = [i**2 for i in a]
c = [i if i % 2 != 0 else i * (-1) for i in b ]
print(c)