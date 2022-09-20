altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
imc = peso / (altura * altura)
if imc >= 16 and imc < 16.9:
    print(f'Muito abaixo do peso,{imc}')
elif imc >= 17 and imc < 18.4:
    print(f'Abaixo do peso, {imc}')
elif imc >= 18.5 and imc < 24.9:
    print(f'Peso ideal é {imc}')
else:
    print(f'Você está acima do peso {imc:.2f}')