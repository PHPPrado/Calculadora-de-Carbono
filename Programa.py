# Cálculo do consumo de energia----------

# Variáveis----------
potencia = 850
horas = int(input("Quantas horas de funcionamento diário? "))
dias = 30
consumoKwhM = (potencia * horas * dias) / 1000  # Equação do consumo

print("O consumo mensal do equipamento será de {}" .format(consumoKwhM))


# Cálculo do custo em reais---------

tarifa = 0.68
custoTotal = consumoKwhM * tarifa  # Valor mensal consumido pela máquina

print("O custo de energia mensal consumida pelo equipamento será de: %2.2f" %
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

print("Serão necessárias {} módulos foltovotaicos" .format(modulos))
