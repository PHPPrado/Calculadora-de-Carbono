def potenciaMineradora(tipoCalculo, potenciaMaquina):

    i = (0)

    if tipoCalculo == 1:
        if potenciaMaquina == 1:
            potencia = 3000
        elif potenciaMaquina == 2:
            potencia = 1800
        elif potenciaMaquina == 3:
            potencia = 850

    horas = int(
        input("Digite a quantidade de horas diárias que a máquina ficará ligada: "))

    while (horas == i):
        if (horas == int()):
            dias = 30
            consumoKwhM = (potencia * horas * dias) / \
                1000  # Equação do consumo
            return potencia, consumoKwhM
            i += 1

        else:
            print(
                "Digite um valor do tipo numerico na sua solicitação de horas, tente novamente.")
            horas = 0
            aio = int(input("Digite 0 para repetir: "))
            if (aio == 0):
                break


potenciaMineradora(1, 850)
