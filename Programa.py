#import os
# os.system('cls')

# Cálculo do consumo de energia----------

# Variáveis----------
potencia = 850
horas = int(
    input("Digite a média de horas diárias que a máquina ficará ligada: "))
dias = 30
consumoKwhM = (potencia * horas * dias) / 1000  # Equação do consumo

print("O consumo mensal do equipamento será de {} Kwh/mês" .format(consumoKwhM))


# Cálculo do custo em reais---------

tarifa = 0.68
custoTotal = consumoKwhM * tarifa  # Valor mensal consumido pela máquina

print("O custo de energia mensal consumida por um equipamento será de: %2.2f" %
      round(custoTotal))


# Cálculo da geração de energia fotovoltaica-----------

potencia = 350
horas = 5
rendimento = (1 - 0.20)
energiaGerada = ((potencia * horas * rendimento) /
                 1000) * 30  # Energia mensal gerada por placa

print("O rendimento mensal de um módulo fotovoltaico é de ",
      int(energiaGerada), "kWh")

modulos = 0
geracaoTotal = 0
while geracaoTotal < consumoKwhM:
    geracaoTotal += energiaGerada
    modulos += 1

print("Serão necessários {} módulos foltovotaicos para suprir o consumo da mensal da máquina de {} kWh/mês" .format(
    modulos, consumoKwhM))

# Fator de emissão

fatorEmissao = 0.1264
carbonoEmitido = (consumoKwhM/1000) * fatorEmissao
conversaoKwh = carbonoEmitido * 1000

print("Sua emissão proveniente do consumo de {}Kwh/mês, é de {} Kg de carbono.".format(consumoKwhM, conversaoKwh))
