def tipoCalculo():
    #escolhaCalculo = input(
    #"Qual tipo de cálculo você deseja realizar?\n\nMineração doméstica.....................[1]\nMineração para meu empreendimento.......[2]\n\nDigite o número correspondente a sua escolha: ")

    try:
        escolhaCalculo = int(input(
    "Qual tipo de cálculo você deseja realizar?\n\nMineração doméstica.....................[1]\nMineração para meu empreendimento.......[2]\n\nDigite o número correspondente a sua escolha: "))
        while (escolhaCalculo != 1) and (escolhaCalculo != 2):
            print("_________________________________________________________________________________________________")
            escolhaCalculo = int(input(
    "Opção incorreta, por favor digite uma opção válida! \n Qual tipo de cálculo você deseja realizar?\n\nMineração doméstica.....................[1]\nMineração para meu empreendimento.......[2]\n\nDigite o número correspondente a sua escolha: "))
        return escolhaCalculo
    except ValueError as error:
        print("_________________________________________________________________________________________________\n")
        print("Opção inválida, por favor digite uma opção válida!")
        print("_________________________________________________________________________________________________\n")
    return tipoCalculo()
    


def potenciaResidencial(tipoCalculo):

    try:
        potenciaMaquina = int(input(
                "Para calcular o seu consumo elétrico, selecione qual das opções melhor\nse encaixa na potência do seu equipamento de mineração:\n\nEquipamento de ALTA potência(3000W)..........[1]\nEquipamento de MÉDIA potência(1800W).........[2]\nEquipamento de BAIXA potência(850W)..........[3]\n\nDigite o número correspondente: "))           
        if tipoCalculo == 1:
            if potenciaMaquina == 1:
                potencia = 3000
            elif potenciaMaquina == 2:
                potencia = 1800
            elif potenciaMaquina == 3:
                potencia = 850
            elif (potenciaMaquina > 3) or (potenciaMaquina < 1):
                print("_________________________________________________________________________________________________\n")
                print("Digite uma opção válida!")
                print("_________________________________________________________________________________________________\n")
                return potenciaResidencial(tipoCalculo)
    except ValueError as error:
        print("_________________________________________________________________________________________________\n")
        print("Digite uma opção válida!")
        print("_________________________________________________________________________________________________\n")
        return(potenciaResidencial(tipoCalculo))

    try:
        horas = int(
        input("Digite a quantidade de horas diárias que a máquina ficará ligada: "))
        if (horas < 0) or (horas > 24):
            print("_________________________________________________________________________________________________\n")
            print("Digite uma opção válida!")
            print("_________________________________________________________________________________________________\n")
            return potenciaResidencial(tipoCalculo)
    except ValueError as error:
        print("_________________________________________________________________________________________________\n")        
        print("Digite um valor válido!")
        print("_________________________________________________________________________________________________\n")
        return potenciaResidencial(tipoCalculo)
    dias = 30
    consumoKwhM = (potencia * horas * dias) / 1000  # Equação do consumo
    return potencia, consumoKwhM   



def potenciaIndustrial(tipoCalculo):
    try:     
        escolhaPotencia = int(input(
            "Para calcular o seu consumo elétrico, selecione qual das opções melhor\nse encaixa na potência dos seus equipamentos de mineração:\n\nANTSPACE HK3(with DWT-T) -> (1030 KW de potência)..........[1]\nBitcoin Miner S19 Hydro -> (5451 W de potência)............[2]\nLitecoin Miner L7 -> (3260 W de potência)..................[3]\nInserir potência personalizada.............................[4]\n\nDigite o número correspondente: "))
    except ValueError as error:
        print("_________________________________________________________________________________________________\n")        
        print("Digite um valor válido!")
        print("_________________________________________________________________________________________________\n")
        return potenciaIndustrial(tipoCalculo)

    if tipoCalculo == 2:
        if escolhaPotencia == 1:
            potencia = 1030  # Valores convertidos em KW
        elif escolhaPotencia == 2:
            potencia = 5.4
        elif escolhaPotencia == 3:
            potencia = 3.2
        elif escolhaPotencia == 4:
            try:
                potencia = float(
                input("Digite o valor da potência em Watts: "))
                if potencia < 1:
                    print("_________________________________________________________________________________________________\n")        
                    print("Digite um valor válido!")
                    print("_________________________________________________________________________________________________\n")
                    return potenciaIndustrial(tipoCalculo)
                potencia /= 1000  # Conversão de watts para Kw
            except ValueError as error:
                print("_________________________________________________________________________________________________\n")
                print("Digite uma opção válida!")
                print("_________________________________________________________________________________________________\n")
                return potenciaIndustrial(tipoCalculo)
        elif (escolhaPotencia > 4) or (escolhaPotencia < 1):
            print("_________________________________________________________________________________________________\n")
            print("Digite uma opção válida!")
            print("_________________________________________________________________________________________________\n")
            return potenciaIndustrial(tipoCalculo)

        try: 
            quantMaquinas = int(
                input("Digite quantas máquinas você tem na sua empresa: "))
            if quantMaquinas < 1:
                print("_________________________________________________________________________________________________\n")
                print("Digite uma opção válida!")
                print("_________________________________________________________________________________________________\n") 
                return potenciaIndustrial(tipoCalculo)
        
        except ValueError as error:
            print("_________________________________________________________________________________________________\n")
            print("Digite uma opção válida!")
            print("_________________________________________________________________________________________________\n")
            return potenciaIndustrial(tipoCalculo)

        try:
            horas = int(
            input("Digite a quantidade de horas diárias que as máquinas ficarão ligadas: "))
            if (horas < 1) or (horas > 24):
                print("_________________________________________________________________________________________________\n")
                print("Digite uma quantidade de horas válida!")
                print("_________________________________________________________________________________________________\n")
                return potenciaIndustrial(tipoCalculo)
        except ValueError as error:
            print("_________________________________________________________________________________________________\n")
            print("Digite uma opção válida!")
            print("_________________________________________________________________________________________________\n")
            return potenciaIndustrial(tipoCalculo)
            
    dias = 30
    consumoMwMes = ((potencia * quantMaquinas) * horas * dias) / \
        1000  # Conversão da potencia em Kwh para Mwh
    return potencia, consumoMwMes, quantMaquinas


def tarifaRed(consumokwhM):

    tarifa = consumokwhM * 0.49 #Consumo multiplicado pela tarifa do grupo B
    return tarifa

def tarifaInd(consumoMwhMes):

    conversaoKwh = consumoMwhMes * 1000
    totalEnergia = conversaoKwh * 0.33  # Total em Kw multiplicado pela tarifa
    return totalEnergia


def modFoto(consumo, energia):
    modulos = 0
    geracaoTotal = 0
    while geracaoTotal < consumo:
        geracaoTotal += energia
        modulos += 1
    return modulos


def emissaoDom(consumoKwhM):
    fatorEmissao = 0.1264
    carbonoEmitido = (consumoKwhM/1000) * fatorEmissao
    carbonoKg = carbonoEmitido * 1000
    return carbonoKg


def emissaoInd(consumoMwMes):
    fatorEmissao = 0.1264
    carbonoTonelada = consumoMwMes * fatorEmissao
    return carbonoTonelada


def arvKg(consumoKwhM):
    contadorArvores = 0
    arvore = 0
    while arvore <= emissaoDom(consumoKwhM):
        arvore += 7.4
        contadorArvores += 1
    return contadorArvores


def arvTon(consumoKwhM):
    contadorArvores = 0
    arvore = 0
    while arvore <= emissaoInd(consumoKwhM):
        arvore += 0.0074
        contadorArvores += 1
    return contadorArvores


def calcCred(carbonoEmKg):
    creditos = 0
    preco = 0
    compensado = 0
    while compensado < carbonoEmKg:
        creditos += 1
        preco += 3.00
        compensado += 1000
    return creditos, preco


def credTon(carbonoEmToneladas):
    creditos = 0
    preco = 0
    compensado = 0
    while compensado < carbonoEmToneladas:
        creditos += 1
        preco += 3.00
        compensado += 1
    return creditos, preco

Test Pull request
