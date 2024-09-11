def validadorInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('\033[31mErro!! Valor invalido digite novamente.\033[m')
