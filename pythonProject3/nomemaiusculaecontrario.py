nome = 'Julian Domeneghini'.upper()
nome_invertido_por_letras = ''.join(reversed(nome))

nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

print(f'Nome com letras em maiúsculo: {nome}')
print(f'Nome com letras maiúsculo invertido por letras: {nome_invertido_por_letras}')
print(f'Nome com letras maiúsculo invertido por palavras: {nome_invertido_por_palavras}')
