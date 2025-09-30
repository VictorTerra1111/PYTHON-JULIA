# Faça um programa que solicite ao usuário um número (maior que 1)
# e imprima todos os números pares de 1 até esse número escolhido pelo usuário.

valor = int(input("Digite um numero inteiro maior que 1: "))

if(valor <= 1):
    print("esse numero eh menor ou igual a 1")
else:
    for i in range (valor + 1):
        if(i % 2 == 0):
            print(i)
