def validadorInt(msg):
    """
    Valida a entrada se é um numero inteiro ou não
    msg: mensagem para o input
    return: retorna o valor do input
    """
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('\033[31mErro!! Valor invalido digite novamente.\033[m')
