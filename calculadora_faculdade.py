class Calculadora:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def soma(self):
        print('A soma é:', self.x + self.y)

    def subtracao(self):
        print('A soma é:', self.x - self.y)

    def multiplicacao(self):
        print('A soma é:', self.x * self.y)

    def divide(self):
        print('A soma é:', self.x / self.y)

    def exponenciacao(self):
        print('A soma é:', self.x ** self.y)

    def modulo(self):
        print('A soma é:', self.x % self.y)


while True:

    print("""Entre com a opção desejada?

    1 -> Somar
    2 -> Subtrair
    3 -> Multiplicação
    4 -> Divisão
    5 -> Exponenciação
    6 -> Modulo
    7 -> Sair""")

    option: str = input("\nEscolha a opção desejada (1,2,3,4,5,6,7)")

    if option == '1':
        P = int(input('Digite o seu penultimo RU:'))
        R = int(input('Digite o seu penultimo RU:'))
        result = P + R
        print(f"A soma é de: {result}")

    elif option == '2':
        P = int(input('Digite o seu penultimo RU:'))
        R = int(input('Digite o seu penultimo RU:'))
        result = P - R
        print(f'A subtracao é de: {result}')

    elif option == '3':
        P = int(input('Digite o seu penultimo RU:'))
        R = int(input('Digite o seu penultimo RU:'))
        result = P * R
        print(f'A multiplicacao é de: {result}')

    elif option == '4':
        P = int(input('Digite o seu penultimo RU:'))
        R = int(input('Digite o seu penultimo RU:'))
        result = P / R
        print(f'A divisão é de: {result}')

    elif option == '5':
        P = int(input('Digite o seu penultimo RU:'))
        R = int(input('Digite o seu penultimo RU:'))
        result = P ** R
        print(f'A exponenciação é de: {result}')

    elif option == '6':
        P = int(input('Digite o seu penultimo RU:'))
        R = int(input('Digite o seu penultimo RU:'))
        result = P % R
        print(f'O modulo é de: {result}')

    elif option == '7':
        break

    else:
        print('Número inválido!')
        continue

