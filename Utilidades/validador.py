def validadorInt(msg):
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('Erro!! Valor invalido digite novamente.')
