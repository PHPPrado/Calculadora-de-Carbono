

def modulosFotovoltaicos(consumo, energia):
    modulos = 0
    geracaoTotal = 0
    while geracaoTotal < consumo:
        geracaoTotal += energia
        modulos += 1
    return modulos


def calcFatorEmissao(consumoKwhM):
    fatorEmissao = 0.1264
    carbonoEmitido = (consumoKwhM/1000) * fatorEmissao
    carbonoKg = carbonoEmitido * 1000
    return carbonoKg


def quantArvores(consumoKwhM):
    contadorArvores = 0
    arvore = 0
    while arvore <= calcFatorEmissao(consumoKwhM):
        arvore += 7.4
        contadorArvores += 1
    return contadorArvores
