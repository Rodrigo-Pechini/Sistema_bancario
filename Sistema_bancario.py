from Utilidades import transações
from Utilidades import validador
from Utilidades import interface
import pytz
from datetime import datetime



DATA_HORA_SP = datetime.now(pytz.timezone('America/Sao_Paulo'))
DATA_HORA_ATUAL = DATA_HORA_SP.strftime('%d/%m/%Y %H:%M')

saldo_total = 0
operacoes = 0
extrato = []

while True:
    interface.menuDeUsuarios()
    interface.menuDeOperacoes()
    opc = validador.validadorInt('Digite uma das opções: ')

    #Depositando um valor no saldo total e no deposito
    if opc == 1:
        deposito = transações.deposito(operacoes)
        if type(deposito) == type(int()):
            saldo_total += deposito
            extrato.append(f'Deposito de R${deposito:.2f} as {DATA_HORA_ATUAL}')
            operacoes += 1
        else:
            print(deposito)

    #Retirando um valor do saldo_total
    elif opc == 2:
        saque = transações.saque(operacoes,saldo_total=saldo_total)
        if type(saque) == type(int()):
            saldo_total -= saque
            extrato.append(f'Saque de R${saque} as {DATA_HORA_ATUAL}')
            operacoes += 1
        else:
            print(saque)
    #Exibindo o extrato do ultimo deposito e o ultimo saque
    elif opc == 3:
        if len(extrato) > 0:
            transações.extrato(extrato)
        else:
            print('Nenhuma operação foi feita.')
        print(f'saldo: R${saldo_total:.2f}')

    #sair do programa/banco
    elif opc == 4:
        break

    else:
        print('\033[31mERRO!! Digite um dos valores no menu.\033[m')
print('VOLTE SEMPRE!')
