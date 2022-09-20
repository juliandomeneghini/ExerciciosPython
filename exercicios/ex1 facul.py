print('Bem Vindo a Pizzaria do Julian Domeneghini')
print('------------------------Cardápio-------------------')
print('|' ' Código' '|' ' Descrição' ' ' ' ' ' | Pizza Média' ' | ' 'Pizza Grande|')
print('|' '  21 ' ' ' ' |' ' Napolitana ' ' ' '| ' 'R$ 20, 00  ' ' |' ' R$ ' ' 26,00 ' ' ' ' |')
print('|' '  22 ' ' ' ' |' ' Napolitana ' ' ' '| ' 'R$ 20, 00  ' ' |' ' R$ ' ' 26,00  ' ' |')
print('|' '  23 ' ' ' ' |' ' Calabresa ' ' ' ' | ' 'R$ 25, 00  ' ' |' ' R$ ' ' 32,50 ' ' ' ' |')
print('|' '  24 ' ' ' ' |' ' Toscana' ' ' ' ' '   | ' 'R$ 30, 00  ' ' |' ' R$ ' ' 39,00  ' ' |')
print('|' '  25 ' ' ' ' |' ' Portuguesa' ' ' ' | ' 'R$ 30, 00  ' ' |' ' R$ ' ' 39,00 ' ' ' ' |')
print('---------------------------------------------------')

tamanho = input('Qual o tamanho da pizza que deseja (M/G): ')
codigo = int(input('Entre com o código do sabor desejado: '))

if codigo == 21 and tamanho == 'M':
    pizza_m = 20
    print('Você pediu uma Pizza Napolitana')
elif codigo == 21 and tamanho == 'G':
    pizza_g = 26
    print('Você pediu uma Pizza Napolitana')

elif codigo == 22:
    print('Você pediu uma Pizza Margherita')

elif codigo == 23:
    print('Você pediu uma Pizza Calabresa')

elif codigo == 24:
    print('Você pediu uma Pizza Toscana')

elif codigo == 25:
    print('Você pediu uma Pizza Portuguesa')

pedido = input('Deseja pedir mais alguma coisa? 1 - Sim ou 0 - Não')
while pedido == '1':
    tamanho = input('Qual o tamanho da pizza que deseja (M/G): ')
    codigo = int(input('Entre com o código do sabor desejado: '))
    if codigo == 21:
        print('Você pediu uma Pizza Napolitana')

    elif codigo == 22:
        print('Você pediu uma Pizza Margherita')

    elif codigo == 23:
        print('Você pediu uma Pizza Calabresa')

    elif codigo == 24:
        print('Você pediu uma Pizza Toscana')

    elif codigo == 25:
        print('Você pediu uma Pizza Portuguesa')

    pedido = input('Deseja pedir mais alguma coisa? 1 - Sim ou 0 - Não ')
    if pedido == '0':
        print('0')
        break

print('O total a ser pago é: ')
