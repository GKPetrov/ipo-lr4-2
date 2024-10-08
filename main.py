a = [int(input("Введите элементы списка")) for i in range(1,6)]
b=[a[i]**2 for i in range(len(a))]
print(b)