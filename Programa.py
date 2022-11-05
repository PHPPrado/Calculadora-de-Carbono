import os
import Calculos
os.system('cls')

# ----------------------------------------------------------------------------------------------------------
repetir = 1
while repetir == 1:
    print("Bem vindo, com este programa você poderá ter acesso aos índices\nde emissões de CO2 do seu empreendimento, ou de sua pessoa física.\n")


    # Escolher o tipo de cálculo, domestico ou empresarial

    tipoCalculo = Calculos.tipoCalculo()

    # Cálculo para consumo domestico
    if tipoCalculo == 1:

        # Cálculo do consumo de energia (Residencial)----------

        print("\n----Cálculo do consumo de energia de um equipamento de mineração----\n")

        # Escolher a potencia:
    
        potencia, consumoKwhM = Calculos.potenciaResidencial(tipoCalculo)
        print("_________________________________________________________________________________________________")
        print("\nO consumo mensal do equipamento será de {} Kwh/mês" .format(consumoKwhM))

        # Cálculo do custo em reais (Residencial)---------

        tarifa = Calculos.tarifaRed(consumoKwhM)

        print("O preço da energia mensal consumida por um equipamento de mineração será de: R$%2.2f \n" %
            round(tarifa, 2))

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
            Calculos.modFoto(consumoKwhM, energiaGerada), consumoKwhM))

        # Fator de emissão (Residencial)

        print("_________________________________________________________________________________________________")
        print("Emissão de carbono gerada pela máquina de mineração:")

        print("Sua emissão proveniente do consumo de {} Kwh/mês, é de {} Kg de carbono. \n"
            .format(consumoKwhM, round(Calculos.emissaoDom(consumoKwhM), 2)))

        # Compensar emissão por reflorestamento (Residencial)------------

        print("Formas de compensar o carbono emitido pela máquina mineradora:")

        print("Para compensar {} quilos de carbono emitidos, é necessário plantar {} árvores" .format(
            round(Calculos.emissaoDom(consumoKwhM), 2), Calculos.arvKg(consumoKwhM)))

        # Calculo de créditos de carbono (Residencial)--------

        carbonoEmKg = Calculos.emissaoDom(
            consumoKwhM)  # Carbono emitido pela máquina
        creditos, preco = Calculos.calcCred(carbonoEmKg)

        print("ou será necessário adquirir {} créditos de carbono por U${}.".format(
            creditos, preco))

        
        repetir = int(input(" \nDigite 1 para executar o programa novamente! \nDigite 0 para sair!\n"))

    # ------------------------------------------------------------------------------------------------------

    # Cálculo para consumo industrial
    elif tipoCalculo == 2:

        # Cálculo do consumo de energia (Industrial) ----------

        print("\n----Cálculo do consumo de energia de um equipamento de mineração----\n")

        potencia, consumoMwMes, quantMaquinas = Calculos.potenciaIndustrial(
            tipoCalculo)
        print("_________________________________________________________________________________________________")
        print("O consumo mensal de {} equipamento(s) será de {} Mwh/mês" .format(
            quantMaquinas, consumoMwMes))

        # Cálculo do custo em reais (Industrial) ---------

        tarifaIndustrial = Calculos.tarifaInd(consumoMwMes)
        print("Aplicadas as taxas sob o consumo elétrico mensal de %2.2f, será cobrado\no valor de R$%2.2f pelo orgão responsável.\n" %(consumoMwMes, tarifaIndustrial))

        # Cálculo da geração de energia fotovoltaica (Industrial)-----------
        print("_________________________________________________________________________________________________")
        print("Para controlar seus gastos com energia, recomendamos a instalação de módulos fotovoltaicos")

        potencia = 0.00035  # Valor em Mega-watt
        horas = 5
        rendimento = (1 - 0.20)
        energiaGerada = (potencia * horas * rendimento) * \
            30  # Energia mensal em mega-watts gerada por placa

        print("O rendimento mensal de um módulo fotovoltaico é de",
            float(round(energiaGerada, 3)), "MW \n")
        # Calculo quantidade de módulos fotovoltaicos (Industrial)---------------

        print("Serão necessários {} módulos foltovotaicos para suprir o consumo da mensal das máquinas mineradoras de {} MWh/mês \n" .format(
            Calculos.modFoto(consumoMwMes, energiaGerada), consumoMwMes))

        # Fator de emissão (Industrial)
        print("_________________________________________________________________________________________________")
        print("Emissão de carbono gerada pelas máquinas de mineração:")

        carbonoTonelada = Calculos.emissaoInd(consumoMwMes)

        print("Sua emissão proveniente do consumo de {} Mw/mês, é de {} toneladas de carbono. \n"
            .format(consumoMwMes, round(carbonoTonelada, 2)))

        # Compensar emissão por reflorestamento (Industrial)------------

        print("Formas de compensar o carbono emitido pelas máquinas mineradoras:")

        print("Para compensar {} toneladas de carbono emitidos, é necessário plantar {} árvores" .format(
            round(carbonoTonelada, 2), Calculos.arvTon(consumoMwMes)))

        # Calculo de créditos de carbono(Industrial)--------

        carbonoEmToneladas = carbonoTonelada  # Carbono emitido pela máquina
        creditos, preco = Calculos.credTon(carbonoEmToneladas)

        print("ou será necessário adquirir {} créditos de carbono por U${}.".format(
            creditos, preco))
        
        repetir = int(input(" \nDigite 1 para executar o programa novamente! \nDigite 0 para sair!\n"))