# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Exemplo: 5! = 5.4.3.2.1 = 120.

valor = int(input("digite um valor para descobrir o fatorial: "))

final = 1

for i in range(1, valor + 1):
    final = final * i

print(f"O fatorial de {valor} eh {final}")
