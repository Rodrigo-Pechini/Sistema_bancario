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
usuarios  = [{4545: {'nome': 'Rodrigo', 'ano': 2004, 'saldo': 0}},
              {4444: {'nome': 'Nana', 'ano': 2005, 'saldo': 0}}, 
              {9999: {'nome': 'Paulo', 'ano': 2012, 'saldo': 0}}, 
              {9898: {'nome': 'Carlos', 'ano': 2006, 'saldo': 0}}]

while True:
    interface.menuDeUsuarios()
    opc = validador.validadorInt('Digite uma das opções: ')
    if opc == 1:
        cadastro = transações.cadastrarUsuarios(usuarios)
        if cadastro != None:
            usuarios.append(cadastro)
    elif opc == 2:
        transações.mostrarUsuario(usuarios)
    elif opc == 3:
        while True:
            #cpf = validador.validadorInt('Digite o CPF do usuario: ')
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
                print(extrato)
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
    elif opc == 4:
        break
    else:
        print('\033[31mERRO!! Digite um dos valores no menu.\033[m')
        
print('VOLTE SEMPRE!')
