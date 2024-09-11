from Utilizades import validador

def deposito(operacoes):
    while True:
        if operacoes < 10:
            valor = validador.validadorInt('Deposito de R$')
            if valor > 0:
                print(f'\033[32mDeposito de R${valor} foi efetuado\033[m')
                return valor
            else:
                    print('\033[31mDigite um valor valido para deposito\033[m')
        else:
             return '\033[31mErro!! Limite de operações diarias atingido\033[m'
        
def saque(operacoes, saldo_total):
    while True:
        if operacoes < 10:
            valor = validador.validadorInt('Saque de R$')
            if saldo_total == 0:
                return '\033[31mErro!! Saldo insuficiente.\033[m'
            if saldo_total < valor:
                return '\033[31mERRO!! Valor para sacar superior ao na conta\033[m'
            elif valor > 500:
                print('\033[31mErro!! O maximo que se pode retirar é R$500\033[m')
            else:
                print(f'\033[32mSaque de R${valor} foi efetuado\033[m')
                return valor     
        else:
            return '\033[31mErro!! Limite de operações diarias atingido\033[m'

def extrato(extrato):
    for e, v in enumerate(extrato):
        print(f'Nº {e+1} | {v}')
