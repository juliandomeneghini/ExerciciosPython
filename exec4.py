sexo = input(
    'Digite o seu sexo. (M para Masculino, F para Feminino, I para Indefinido: )').upper()
if sexo == 'M':
    print('Masculino')
elif sexo == 'F':
    print('Feminino')
elif sexo == 'I':
    print('Indefinido')
else:
    print('Sexo Inválido')
