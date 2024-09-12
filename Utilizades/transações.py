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



def cadastrarUsuarios(usuarios):

    cpf = validador.validadorInt('Digite seu CPF: ')
    pessoa  = {}
    cadastro = {}
    pessoa["nome"] = str(input('Digite seu nome: '))
    pessoa["ano"] = validador.validadorInt('Digite o ano de nascimento: (XXXX) ')
    cadastro[cpf] = pessoa

    return cadastro


def mostrarUsuario(usuarios):
    for u in usuarios:
        for i in u.keys():
            print(f"CPF = {i} | nome = {u[i]['nome']} | ano = {u[i]['ano']}")

"""
def usuarioCadastrados(usuarios, cpf):
    rps = False
    for u in usuarios:
        for i in u.keys():
            if i == cpf:
                rps = True
    return rps
        """