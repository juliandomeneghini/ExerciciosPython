lista = []

while True:
    nome = input('Informe seu nome: ')
    nota1 = float(input('Digite uma nota: '))
    nota2 = float(input('Digite uma nota: '))
    nota3 = float(input('Digite uma nota: '))
    lista.append([nome, [nota1, nota2, nota3]])
    resposta = str(input('Próximo Aluno? [S/N] '))

    if resposta in 'S':
        continue
    else:
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}')
print('-' * 26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? '))
    if opc == 10:
        print('Finalizando...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('Notas concluídas')
