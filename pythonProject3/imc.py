print('---------- Lojas Martin ----------')
preco = float(input('Preco das compras: R$ '))
print('''
FORMAS DE PAGAMENTO
[1] á vista em dinheiro / cheque: 10% de desconto.
[2] á vista no cartão de crédito: 5% de desconto.
[3] em até 2x no cartão de crédito preço normal.
[4] 3x ou mais no cartão de crédito 10% de juros.
''')
opc = int(input('Qual é a opção? '))
if opc == 1:
    total = preco - (preco * 10 / 100)

elif opc == 2:
    total = preco - (preco * 5 / 100)

elif opc == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros'.format(parcela))

elif opc == 4:
    total = preco + (preco * 10 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totalparc, parcela))

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
