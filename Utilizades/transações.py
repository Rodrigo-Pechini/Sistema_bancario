from Utilizades import validador

def transacao(msg):
    while True:
        valor = validador.validadorInt(msg)
        if valor > 0:
            return valor
        print('Erro!! valor invalido')

def extrato(extrato):
    for e, v in enumerate(extrato):
        print(f'Nº {e+1} | {v}')
