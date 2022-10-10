import os
os.system('cls')

print("Bem vindo, com este programa você poderá ter acesso aos índices de emissões de CO2 do seu empreendimento, ou de sua pessoa física.\n")


# Cálculo do consumo de energia----------

print("Calculo do consumo de energia de um equipamento de mineração: \n")
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

modulos = 0
geracaoTotal = 0
while geracaoTotal < consumoKwhM:
    geracaoTotal += energiaGerada
    modulos += 1

print("Serão necessários {} módulos foltovotaicos para suprir o consumo da mensal da máquina mineradora de {} kWh/mês \n" .format(
    modulos, consumoKwhM))

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
