import os
import Calculos
os.system('cls')

print("Bem vindo, com este programa você poderá ter acesso aos índices\nde emissões de CO2 do seu empreendimento, ou de sua pessoa física.\n")


# Escolher o tipo de cálculo, domestico ou empresarial
tipoCalculo = int(input(
    "Qual tipo de cálculo você deseja realizar?\n\nMineração domestica.....................[1]\nMineração para meu empreendimento.......[2]\n\nDigite o número correspondente a sua escolha: "))


# Cálculo para consumo domestico---------
if tipoCalculo == 1:

    # Cálculo do consumo de energia----------

    print("\n----Calculo do consumo de energia de um equipamento de mineração----\n")

    # Escolher a potencia:
    # /
    # /
    # /
    # /
    # /

    potencia = 850
    horas = int(
        input("Digite a quantidade de horas diárias que a máquina ficará ligada: "))
    dias = 30
    consumoKwhM = (potencia * horas * dias) / 1000  # Equação do consumo

    print("\nO consumo mensal do equipamento será de {} Kwh/mês" .format(consumoKwhM))

    # Cálculo do custo em reais---------

    #

    tarifa = 0.68
    custoTotal = consumoKwhM * tarifa  # Valor mensal consumido pela máquina

    print("O preço da energia mensal consumida por um equipamento de mineração será de: R$%2.2f \n" %
          round(custoTotal))

    # Cálculo da geração de energia fotovoltaica-----------

    print("Módulos fotovoltaicos ")

    potencia = 350
    horas = 5
    rendimento = (1 - 0.20)
    energiaGerada = ((potencia * horas * rendimento) /
                     1000) * 30  # Energia mensal gerada por placa

    print("O rendimento mensal de um módulo fotovoltaico é de ",
          int(energiaGerada), "kWh \n")

    #modulos = 0
    #geracaoTotal = 0
    # while geracaoTotal < consumoKwhM:
    #    geracaoTotal += energiaGerada
    #   modulos += 1

    print("Serão necessários {} módulos foltovotaicos para suprir o consumo da mensal da máquina mineradora de {} kWh/mês \n" .format(
        Calculos.modulosFotovoltaicos(consumoKwhM, energiaGerada), consumoKwhM))

    # Fator de emissão

    print("Emissão de carbono gerada pela máquina de mineração:")

    print("Sua emissão proveniente do consumo de {} Kwh/mês, é de {} Kg de carbono. \n"
          .format(consumoKwhM, round(Calculos.calcFatorEmissao(consumoKwhM), 2)))

    # Compensar emissão por reflorestamento------------

    print("Formas de compensar o carbono emitido pela máquina mineradora:")

    print("Para compensar {} quilos de carbono emitidos, é necessário plantar {} árvores" .format(
        round(Calculos.calcFatorEmissao(consumoKwhM), 2), Calculos.quantArvores(consumoKwhM)))

    # Calculo de créditos de carbono--------

    creditos = 0
    preco = 0
    compensado = 0
    while compensado < Calculos.calcFatorEmissao(consumoKwhM):
        creditos += 1
        preco += 3.00
        compensado += 1000

    print("Ou será necessário adquirir {} créditos de carbono por U${}.".format(
        creditos, preco))

elif tipoCalculo == 2:
    # Cálculo do consumo de energia----------

    print("\n----Calculo do consumo de energia de um equipamento de mineração----\n")
    potencia = 850
    horas = int(
        input("Digite a quantidade de horas diárias que a máquina ficará ligada: "))
    dias = 30
    consumoKwhM = (potencia * horas * dias) / 1000  # Equação do consumo

    print("O consumo mensal do equipamento será de {} Kwh/mês" .format(consumoKwhM))

    # Cálculo do custo em reais---------

    tarifa = 0.68
    custoTotal = consumoKwhM * tarifa  # Valor mensal consumido pela máquina

    print("O preço da energia mensal consumida por um equipamento de mineração será de: R$%2.2f \n" %
          round(custoTotal))

    # Cálculo da geração de energia fotovoltaica-----------

    print("Módulos fotovoltaicos ")

    potencia = 350
    horas = 5
    rendimento = (1 - 0.20)
    energiaGerada = ((potencia * horas * rendimento) /
                     1000) * 30  # Energia mensal gerada por placa

    print("O rendimento mensal de um módulo fotovoltaico é de ",
          int(energiaGerada), "kWh \n")

    #modulos = 0
    #geracaoTotal = 0
    # while geracaoTotal < consumoKwhM:
    #    geracaoTotal += energiaGerada
    #    modulos += 1

    print("Serão necessários {} módulos foltovotaicos para suprir o consumo da mensal da máquina mineradora de {} kWh/mês \n" .format(
        Calculos.modulosFotovoltaicos(consumoKwhM, energiaGerada), consumoKwhM))

    # Fator de emissão

    print("Emissão de carbono gerada pela máquina de mineração:")

    fatorEmissao = 0.1264
    carbonoEmitido = (consumoKwhM/1000) * fatorEmissao
    carbonoKg = carbonoEmitido * 1000

    print("Sua emissão proveniente do consumo de {} Kwh/mês, é de {} Kg de carbono. \n"
          .format(consumoKwhM, round(carbonoKg, 2)))

    # Compensar emissão por reflorestamento------------

    print("Formas de compensar o carbono emitido pela máquina mineradora:")

    contadorArvores = 0
    arvore = 0
    while arvore <= carbonoKg:
        arvore += 7.4
        contadorArvores += 1

    print("Para compensar {} quilos de carbono emitidos, é necessário plantar {} árvores" .format(
        round(carbonoKg, 2), contadorArvores))

    # Calculo de créditos de carbono--------

    creditos = 0
    preco = 0
    compensado = 0
    while compensado < carbonoKg:
        creditos += 1
        preco += 3.00
        compensado += 1000

    print("Ou será necessário adquirir {} créditos de carbono por U${}.".format(
        creditos, preco))
