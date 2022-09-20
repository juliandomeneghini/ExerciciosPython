preco = 0  # Preco começa com o valor ZERO
print('Bem-Vindo a Pizzaria do Julian Domeneghini')  # Identificador Pessoal

# Exibe o Cardápio
print('------------------------Cardápio-------------------')
print("| Código | Descrição   | Pizza Média |  Pizza Grande|")
print("|  21    | Napolitana  | R$ 20, 00   |  R$  26,00   |")
print("|  22    | Margherita  | R$ 20, 00   |  R$  26,00   |")
print("|  23    | Calabresa   | R$ 25, 00   |  R$  32,50   |")
print("|  24    | Toscana     | R$ 30, 00   |  R$  39,00   |")
print("|  25    | Portuguesa  | R$ 30, 00   |  R$  39,00   |")
print("---------------------------------------------------")

while True:
    tamanho = input('Qual o tamanho de pizza que deseja (M/G): ')
    # Verifica se os tamanhos diferem de M e G
    if (tamanho != 'M') and (tamanho != 'G'):
        # se diferem, então ele exibe "Opção Inválida"
        print("Opção Inválida")
        continue  # Volta para o início do laço de repetição

    codigo = int(input('Entre com o código do sabor desejado: '))
    if 20 < codigo > 26:  # Se codigo for menor de 20 e maior de 26
        print("Opção Inválida")  # Exibe a mensagem na tela de "Opção Inválida"
        continue  # Volta para o laço de repetição
    if tamanho == 'M' and codigo == 21:
        preco += 20
        print('Você pediu uma Pizza Napolitana')
    elif tamanho == 'G' and codigo == 21:
        preco += 26
        print('Você pediu uma Pizza Napolitana')
    elif tamanho == 'M' and codigo == 22:
        preco += 20
        print('Você pediu uma Pizza Margherita')
    elif tamanho == 'G' and codigo == 22:
        preco += 26
        print('Você pediu uma Pizza Margherita')
    elif tamanho == 'M' and codigo == 23:
        preco += 25
        print('Você pediu uma Pizza Calabresa')
    elif tamanho == 'G' and codigo == 23:
        preco += 32.50
        print('Você pediu uma Pizza Calabresa')
    elif tamanho == 'M' and codigo == 24:
        preco += 30
        print('Você pediu uma Pizza Toscana')
    elif tamanho == 'G' and codigo == 24:
        preco += 39
        print('Você pediu uma Pizza Toscana')
    elif tamanho == 'M' and codigo == 25:
        preco += 30
        print('Você pediu uma Pizza Portuguesa')
    elif tamanho == 'G' and codigo == 25:
        preco += 39  #
        print('Você pediu uma Pizza Portuguesa')
    else:
        print("Opção Inválida")  # Exibe a mensagem na tela de "Opção Inválida"
        continue

    resposta = input('Deseja pedir mais alguma coisa? \n 1 - Sim\n 0 - Não\n >> ')  # Pergunta ao cliente
    if resposta == '1':
        continue  # Volta para o início do laço de repetição

    else:
        print('O total a ser pago é: R$ {:.2f}'.format(preco))
        break  # comando para sair do “loop” While
