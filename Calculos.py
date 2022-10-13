

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


def calculoCreditos(carbonoEmKg):
    creditos = 0
    preco = 0
    compensado = 0
    while compensado < carbonoEmKg:
        creditos += 1
        preco += 3.00
        compensado += 1000

    return creditos, preco


def potenciaMineradora(tipoCalculo, potenciaMaquina):

    if tipoCalculo == 1:
        if potenciaMaquina == 1:
            potencia = 3000
        elif potenciaMaquina == 2:
            potencia = 1800
        elif potenciaMaquina == 3:
            potencia = 850

    elif tipoCalculo == 2:
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
