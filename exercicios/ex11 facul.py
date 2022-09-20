listaprodutos = []


# Inicio do Cadastro de Produto =
def cadastrarproduto(codigo):
    print('Você selecionou a opção Cadastrar Produto')
    print('Código do produto: {}'.format(codigo))
    nome = input('Por favor entre com o NOME da Produto: ')
    fabricante = input('Por favor entre com o FABRICANTE: ')
    valor = float(input('Por favor entre com o VALOR(R$) do Produto: '))
    dict_produtos = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante, 'valor': valor}
    listaprodutos.append(dict_produtos.copy())
    dict_produtos.clear()


# Fim do Cadastro de Produto

# Inicio do Consulta Produto
def consultaproduto():
    while True:
        print('Você selecionou a Opção de consultar Produtos')
        opconsulta = int(input('Escolha a opção desejada:\n'
                               '1 - Consultar Todos os Produtos\n'
                               '2 - Consultar Produtos por Código\n'
                               '3 - Consultar Produtos por Fabricante\n'
                               '4- Retornar\n>>)'))
        if opconsulta == 1:
            print('--------------------')
            for lista in listaprodutos:
                for key, value in lista.items():
                    print('{} : {}'.format(key, value))
            print('--------------------')
        elif opconsulta == 2:
            entrada = int(input('Digite o CÓDIGO do Produto: '))
            print('--------------------')
            for lista in listaprodutos:
                if lista['codigo'] == entrada:
                    for key, value in lista.items():
                        print('{} : {}'.format(key, value))
            print('--------------------')
        elif opconsulta == 3:
            entrada = input('Digite o FABRICANTE do(s) Produto(s): ')
            print('--------------------')
            for lista in listaprodutos:
                if lista['fabricante'] == entrada:
                    for key, value in lista.items():
                        print('{} : {}'.format(key, value))
            print('--------------------')

        elif opconsulta == 4:
            break
# Fim da Consulta do Produto

# Inicio do remove Produtos


def removeproduto():
    print('Você selecionou remover Produto')
    entrada = int(input('Digite o código do Produto para ser removido: '))
    for lista in listaprodutos:
        if lista['codigo'] == entrada:
            listaprodutos.remove(lista)
    # Fim do remove Produto

    # Inicio do Programa


print('Bem-vindo ao Controle de Estoque da Mercearia do Julian Domeneghini')
registroSistema = 0  # Inicia a função com valor inicial de 0
while True:
    opcao = int(input('Escolha a opção desejada:\n'
                      '1 - Cadastrar Produto\n'
                      '2 - Consultar Produto(s)\n'
                      '3 - Remover Produto\n'
                      '4- Sair\n>>)'))
    if opcao == 1:
        registroSistema = registroSistema + 1
        cadastrarproduto(registroSistema)

    elif opcao == 2:
        consultaproduto()

    elif opcao == 3:
        removeproduto()

    elif opcao == 4:
        print('Sair')
        break
# Fim do programa
