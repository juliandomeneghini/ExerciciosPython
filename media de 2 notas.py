nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite outra nota:'))
media = (nota1+nota2)/2
print(f'Sua media foi: {media}')
if media >= 6 and media <= 7:
    print('Aprovado')
elif media == 10:
    print('Aprovado com Distinção!')
else:
    print('Reprovado')
