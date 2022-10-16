def potenciaMineradora(tipoCalculo, potenciaMaquina):

    if tipoCalculo == 1:
        if potenciaMaquina == 1:
            potencia = 3000
        elif potenciaMaquina == 2:
            potencia = 1800
        elif potenciaMaquina == 3:
            potencia = 850

    horas = int(
        input("Digite a quantidade de horas diárias que a máquina ficará ligada: "))
    dias = 30
    consumoKwhM = (potencia * horas * dias) / 1000  # Equação do consumo
    return potencia, consumoKwhM


def potenciaIndustrial(tipoCalculo, potenciaMaquina):

    if tipoCalculo == 2:
        if potenciaMaquina == 1:
            potencia = 1030
        elif potenciaMaquina == 2:
            potencia = 5.4
        elif potenciaMaquina == 3:
            potencia = 3.2
        elif potenciaMaquina == 4:
            potencia = int(input("Digite o valor da potência em QuiloWatts: "))

        quantMaquinas = int(
            input("Digite quantas maquinas você tem na sua empresa: "))

        horas = int(
            input("Digite a quantidade de horas diárias que as máquinas ficarão ligadas: "))
    dias = 30
    consumoMwMes = ((potencia * quantMaquinas) * horas * dias) / \
        1000  # Conversão da potencia em Kwh para Mwh
    return potencia, consumoMwMes, quantMaquinas


def modulosFotovoltaicos(consumo, energia):
    modulos = 0
    geracaoTotal = 0
    while geracaoTotal < consumo:
        geracaoTotal += energia
        modulos += 1
    return modulos


def calcFatorEmissaoDomestico(consumoKwhM):
    fatorEmissao = 0.1264
    carbonoEmitido = (consumoKwhM/1000) * fatorEmissao
    carbonoKg = carbonoEmitido * 1000
    return carbonoKg


def calcFatorEmissaoIndustrial(consumoMwMes):
    fatorEmissao = 0.1264
    carbonoTonelada = consumoMwMes * fatorEmissao
    return carbonoTonelada


def quantArvoresQuilos(consumoKwhM):
    contadorArvores = 0
    arvore = 0
    while arvore <= calcFatorEmissaoDomestico(consumoKwhM):
        arvore += 7.4
        contadorArvores += 1
    return contadorArvores


def quantArvoresToneladas(consumoKwhM):
    contadorArvores = 0
    arvore = 0
    while arvore <= calcFatorEmissaoIndustrial(consumoKwhM):
        arvore += 0.0074
        contadorArvores += 1
    return contadorArvores


def calculoCreditos(carbonoEmKg):
    creditos = 0
    preco = 0
    compensado = 0
    while compensado < carbonoEmKg:
        creditos += 1
        preco += 3.00
        compensado += 1000
    return creditos, preco


def calculoCreditosTon(carbonoEmToneladas):
    creditos = 0
    preco = 0
    compensado = 0
    while compensado < carbonoEmToneladas:
        creditos += 1
        preco += 3.00
        compensado += 1
    return creditos, preco
