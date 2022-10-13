import os
import Calculos
os.system('cls')

# ----------------------------------------------------------------------------------------------------------
print("Bem vindo, com este programa você poderá ter acesso aos índices\nde emissões de CO2 do seu empreendimento, ou de sua pessoa física.\n")


# Escolher o tipo de cálculo, domestico ou empresarial
tipoCalculo = int(input(
    "Qual tipo de cálculo você deseja realizar?\n\nMineração domestica.....................[1]\nMineração para meu empreendimento.......[2]\n\nDigite o número correspondente a sua escolha: "))


# Cálculo para consumo domestico
if tipoCalculo == 1:

    # Cálculo do consumo de energia (Residencial)----------

    print("\n----Calculo do consumo de energia de um equipamento de mineração----\n")

    # Escolher a potencia:

    escolhaPotencia = int(input(
        "Para calcular o seu consumo elétrico, selecione qual das opções melhor\nse encaixa na potência do seu equipamento de mineração:\n\nEquipamento de ALTA potência..........[1]\nEquipamento de MÉDIA potência.........[2]\nEquipamento de BAIXA potência.........[3]\n\nDigite o número correspondente: "))

    potencia, consumoKwhM = Calculos.potenciaMineradora(
        tipoCalculo, escolhaPotencia)

    print("\nO consumo mensal do equipamento será de {} Kwh/mês" .format(consumoKwhM))

    # Cálculo do custo em reais (Residencial)---------

    tarifa = 0.68
    custoTotal = consumoKwhM * tarifa  # Valor mensal consumido pela máquina

    print("O preço da energia mensal consumida por um equipamento de mineração será de: R$%2.2f \n" %
          round(custoTotal))

    # Cálculo da geração de energia fotovoltaica (Residencial)-----------

    print("_________________________________________________________________________________________________")
    print("Para economizar na conta de luz, recomendamos a instalação de módulos fotovoltaicos em sua residência.")

    potencia = 350
    horas = 5
    rendimento = (1 - 0.20)
    energiaGerada = ((potencia * horas * rendimento) /
                     1000) * 30  # Energia mensal gerada por placa

    print("O rendimento mensal de um módulo fotovoltaico é de ",
          int(energiaGerada), "kWh. \n")

    # Calculo da quantidade de módulos fotovoltaicas necessárias (Residencial)
    print("Serão necessários {} módulos fotovoltaicos para suprir o consumo da mensal de {} kWh/mês \n" .format(
        Calculos.modulosFotovoltaicos(consumoKwhM, energiaGerada), consumoKwhM))

    # Fator de emissão (Residencial)

    print("_________________________________________________________________________________________________")
    print("Emissão de carbono gerada pela máquina de mineração:")

    print("Sua emissão proveniente do consumo de {} Kwh/mês, é de {} Kg de carbono. \n"
          .format(consumoKwhM, round(Calculos.calcFatorEmissao(consumoKwhM), 2)))

    # Compensar emissão por reflorestamento (Residencial)------------

    print("Formas de compensar o carbono emitido pela máquina mineradora:")

    print("Para compensar {} quilos de carbono emitidos, é necessário plantar {} árvores" .format(
        round(Calculos.calcFatorEmissao(consumoKwhM), 2), Calculos.quantArvores(consumoKwhM)))

    # Calculo de créditos de carbono (Residencial)--------

    carbonoEmKg = Calculos.calcFatorEmissao(
        consumoKwhM)  # Carbono emitido pela máquina
    creditos, preco = Calculos.calculoCreditos(carbonoEmKg)

    print("ou será necessário adquirir {} créditos de carbono por U${}.".format(
        creditos, preco))

# ------------------------------------------------------------------------------------------------------

# Cálculo para consumo industrial
elif tipoCalculo == 2:
    # Cálculo do consumo de energia (Industrial) ----------

    print("\n----Calculo do consumo de energia de um equipamento de mineração----\n")
    potencia = 850
    horas = int(
        input("Digite a quantidade de horas diárias que a máquina ficará ligada: "))
    dias = 30
    consumoKwhM = (potencia * horas * dias) / 1000  # Equação do consumo

    print("O consumo mensal do equipamento será de {} Kwh/mês" .format(consumoKwhM))

    # Cálculo do custo em reais (Industrial) ---------

    tarifa = 0.68
    custoTotal = consumoKwhM * tarifa  # Valor mensal consumido pela máquina

    print("O preço da energia mensal consumida por um equipamento de mineração será de: R$%2.2f \n" %
          round(custoTotal))

    # Cálculo da geração de energia fotovoltaica (Industrial)-----------

    print("Módulos fotovoltaicos ")

    potencia = 350
    horas = 5
    rendimento = (1 - 0.20)
    energiaGerada = ((potencia * horas * rendimento) /
                     1000) * 30  # Energia mensal gerada por placa

    print("O rendimento mensal de um módulo fotovoltaico é de ",
          int(energiaGerada), "kWh \n")

    # Calculo quantidade de módulos fotovoltaicos (Industrial)---------------

    print("Serão necessários {} módulos foltovotaicos para suprir o consumo da mensal da máquina mineradora de {} kWh/mês \n" .format(
        Calculos.modulosFotovoltaicos(consumoKwhM, energiaGerada), consumoKwhM))

    # Fator de emissão (Industrial)

    print("Emissão de carbono gerada pela máquina de mineração:")

    print("Sua emissão proveniente do consumo de {} Kwh/mês, é de {} Kg de carbono. \n"
          .format(consumoKwhM, round(Calculos.calcFatorEmissao(consumoKwhM), 2)))

    # Compensar emissão por reflorestamento (Industrial)------------

    print("Formas de compensar o carbono emitido pela máquina mineradora:")

    print("Para compensar {} quilos de carbono emitidos, é necessário plantar {} árvores" .format(
        round(Calculos.calcFatorEmissao(consumoKwhM), 2), Calculos.quantArvores(consumoKwhM)))

    # Calculo de créditos de carbono(Industrial)--------

    carbonoEmKg = Calculos.calcFatorEmissao(
        consumoKwhM)  # Carbono emitido pela máquina
    creditos, preco = Calculos.calculoCreditos(carbonoEmKg)

    print("ou será necessário adquirir {} créditos de carbono por U${}.".format(
        creditos, preco))
