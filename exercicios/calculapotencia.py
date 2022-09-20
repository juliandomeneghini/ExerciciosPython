n = input('Digite um número a ser potenciado: ')
n = int(n)

p = input('Digite a potência desejada: ')
p = int(p)

while((p < 0) or (n <= 1)):
    print("Entrada inválida")
    n = input('Digite um número a ser potenciado: ')
    n = int(n)
    p = input('Digite a potência desejada: ')
    p = int(p)

Pote = 1
if p > 0:
    for j in range(1, p + 1):
        Pote = Pote * n
print()
print(n,"elevdo a", p, ":", Pote)