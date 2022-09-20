from main import calcular_lucro, calcular_faturamento


def test_calcular_lucro():
    faturamento = calcular_faturamento()
    assert calcular_lucro(1000, 500) > 0


def test_calcular_faturamento():
    assert type(calcular_faturamento()) == int
