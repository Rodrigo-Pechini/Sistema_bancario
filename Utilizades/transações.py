from Utilizades import validador

def deposito(operacoes):
    '''
    Faz uma verificação do input do usuario para retornar o valor 
    para depositar
    operações: O limite de operações para o usuario
    return: retorna o valor para deposito
    '''
    while True:
        if operacoes < 10:# verifica a quantidades de operações
            valor = validador.validadorInt('Deposito de R$')# Valida o numero inteiro
            if valor > 0:
                print(f'\033[32mDeposito de R${valor} foi efetuado\033[m')
                return valor
            else:
                    print('\033[31mDigite um valor valido para deposito\033[m')
        else:
             return '\033[31mErro!! Limite de operações diarias atingido\033[m'


def saque(operacoes, saldo_total):
    '''
    Faz uma verificação do input do usuario para retornar o valor 
    para o saque
    operações: O limite de operações para o usuario
    saldo_total: O saldo da conta do usuario
    return: retorna o valor para saque
    '''
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
    '''
    Exibe as operações feitas
    Extrato: Uma lista com as operações
    return: Não tem, mas exibe todas as operações feitas
    '''
    for e, v in enumerate(extrato):
        print(f'Nº {e+1} | {v}')



def cadastrarUsuarios(usuarios):
    '''
    Cadastra os dados do usuario em dois dicionarios
    EXEMPLO:
    {Cpf:{'nome': nome, 'ano': ano, 'saldo': saldo}}
    Usario: Uma lista dos usuarios ja cadastrados
    return: retorna o usuario ja cadastrado
    '''
    pessoa  = {}
    cadastro = {}
    cpf = validador.validadorInt('Digite seu CPF: ')
    if usuarioCadastrados(usuarios=usuarios, cpf=cpf ):# Verificando se usuario ja está cadastrado
        return print('Usario ja cadastrado')
    pessoa["nome"] = str(input('Digite seu nome: '))
    pessoa["ano"] = validador.validadorInt('Digite o ano de nascimento: (XXXX) ')
    pessoa['saldo'] = 0
    cadastro[cpf] = pessoa

    return cadastro


def mostrarUsuario(usuarios):
    '''
    Exibe os usuarios ja cadastrados
    Usuario: Uma lista dos usuarios ja cadastrados
    '''
    for u in usuarios:
        for i in u.keys():
            print(f"CPF = {i} | nome = {u[i]['nome']} | ano = {u[i]['ano']}")


def usuarioCadastrados(usuarios, cpf):
    '''
    Indentifica se o usuario ja foi cadastrado ou não
    Usuarios: Uma lista de usuarios
    cpf: O cpf a ser procurado na lista
    return: Se achar o cpf retorna True se não retorna False
    '''
    rps = False
    for u in usuarios:
        for i in u.keys():
            if i == cpf:
                rps = True
    return rps
