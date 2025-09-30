a = int(input("Digite o valor do primeiro numero: "))
b = int(input("Digite o valor do segundo numero: "))

if a < b:
    print(a)
    for i in range(a + 1, b):
        print(i)
    print(b)
elif b < a:
    print(b)
    for i in range(b + 1, a):
        print(i)
    print(a)
else:
    print(a)
