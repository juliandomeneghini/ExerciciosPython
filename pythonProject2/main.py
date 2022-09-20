# sistema gerencial


# calcular o faturamento
def calcular_faturamento():
    vendas = [1000, 2000, 3000, 4000, 5000]
    faturamento = sum(vendas)
    return faturamento


# calcular o custo


# calcular o lucro
def calcular_lucro(faturamento, custo):
    lucro = faturamento - custo
    return lucro


print(calcular_lucro(1000, 500))
