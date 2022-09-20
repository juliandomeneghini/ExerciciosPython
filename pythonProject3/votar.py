from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

if idade == 18:
    print(f'Idade: {idade} anos')
    print('Situação: Já deve se alistar ao serviço militar.')

elif idade < 18:
    id_calculo_menor = 18 - idade
    print('Situação: Ainda é novo para o alistamento.')
    print('Ainda falta {} ano para o alistamento'.format(id_calculo_menor))
elif idade > 18:
    id_calculo_acima = idade - 18
    print(f'Idade: {idade} anos')
    print(f'Situação: Já passou do prazo do alistamento. Está {id_calculo_acima} anos atrasado.')
