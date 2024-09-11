from Utilizades import transações
from Utilizades import validador
from Utilizades import interface
import pytz
from datetime import datetime



DATA_HORA_SP = datetime.now(pytz.timezone('America/Sao_Paulo'))
DATA_HORA_ATUAL = DATA_HORA_SP.strftime('%d/%m/%Y %H:%M')

saldo_total = 0
operacoes = 0
extrato = []

while True:
    
    interface.menu()
    opc = validador.validadorInt('Digite uma das opções: ')

    #Depositando um valor no saldo total e no deposito
    if opc == 1:
        if operacoes < 10:
            deposito = transações.transacao('Deposito de R$')
            if deposito > 0:
                print(f'\033[32mDeposito de R${deposito} foi efetuado\033[m')
                
                saldo_total += deposito
                extrato.append(f'Deposito de {deposito:.2f} as {DATA_HORA_ATUAL}')
                operacoes += 1
                
            else:
                print('Digite um valor valido para deposito')
        else:
            print('\033[31mErro!! Limite de operações diarias atingido\033[m')

    #Retirando um valor do saldo_total
    elif opc == 2:
        if operacoes < 10:
            retirar = transações.transacao('Saque de R$')

            if retirar < saldo_total and retirar <= 500:
                print(f'\033[32mSaque de R${retirar} foi efetuado\033[m')

                saldo_total -= retirar
                extrato.append(f'Saque de {retirar:.2f} as {DATA_HORA_ATUAL}')
                operacoes += 1

            else:
                if retirar > 500 and operacoes < 10:
                    print('\033[31mErro!! O maximo que se pode retirar é R$500\033[m')
                else:
                    print('\033[31mErro!! Saldo insuficiente.\033[m')
        else:
            print('\033[31mErro!! Limite de operações diarias atingido\033[m')
                
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
