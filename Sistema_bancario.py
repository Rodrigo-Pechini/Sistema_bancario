# Importação das funções
from Utilizades import transações
from Utilizades import validador
from Utilizades import interface
import pytz
from datetime import datetime



DATA_HORA_SP = datetime.now(pytz.timezone('America/Sao_Paulo'))# Pega o local de SP
DATA_HORA_ATUAL = DATA_HORA_SP.strftime('%d/%m/%Y %H:%M')# Pega a data e hora atual 

operacoes = 0

usuarios  = [{4545: {'nome': 'Rodrigo', 'ano': 2004, 'saldo': 0}},
              {4444: {'nome': 'Nana', 'ano': 2005, 'saldo': 0}}, 
              {9999: {'nome': 'Paulo', 'ano': 2012, 'saldo': 0}}, 
              {9898: {'nome': 'Carlos', 'ano': 2006, 'saldo': 0}}]

while True:

    interface.menuDeUsuarios()# Mostra um menu principal
    opc = validador.validadorInt('Digite uma das opções: ')# Entrada de usuario

    if opc == 1:
        # Cadastro do usuario
        cadastro = transações.cadastrarUsuarios(usuarios)
        if cadastro != None:# Adiciona o usuario na lista de usuarios
            usuarios.append(cadastro)

    elif opc == 2:
        # Mostra os dados dos usuarios cadastrados
        transações.mostrarUsuario(usuarios)

    elif opc == 3:
        # Manipulação do saldo e estrado da conta de um usuario
        conta_usuario = None
        print('=' * 30)
        print('Qual conta de usuario quer acessar?')
        cpf = validador.validadorInt('Digite o CPF do usuario: ')

        # Indentifica o usario para acessar
        var_control = False
        for u in usuarios:
            for k in u.keys():
                if k == cpf:
                    conta_usuario = u[cpf]
                    var_control = True
                    print(conta_usuario)
                    if 'extrato' not in conta_usuario:
                        conta_usuario['extrato'] = []
                    break
        if var_control:
            while True:

                interface.menuDeOperacoes()
                opc = validador.validadorInt('Digite uma das opções: ')

                #Depositando um valor na conta do usuario
                if opc == 1:
                    deposito = transações.deposito(operacoes)
                    if isinstance(deposito, int):
                        conta_usuario['saldo'] += deposito
                        conta_usuario['extrato'].append(f'Deposito de R${deposito:.2f} as {DATA_HORA_ATUAL}')
                        operacoes += 1
                    else:
                        print(deposito)

                #Retirando um valor da conta do usuario
                elif opc == 2:
                    saque = transações.saque(operacoes,saldo_total=conta_usuario['saldo'])
                    if isinstance(saque, int):
                        conta_usuario['saldo'] -= saque
                        conta_usuario['extrato'].append(f'Saque de R${saque} as {DATA_HORA_ATUAL}')
                        operacoes += 1
                    else:
                        print(saque)

                #Exibindo o extrato do ultimo deposito e o ultimo saque
                elif opc == 3:
                    print('=' * 30)
                    print(f'Visitando o extrato de {conta_usuario["nome"]}')
                    if len(conta_usuario['extrato']) > 0:
                        transações.extrato(conta_usuario['extrato'])
                    else:
                        print('Nenhuma operação foi feita.')
                    print(f'saldo: R${conta_usuario["saldo"]:.2f}')

                #sair do programa/banco
                elif opc == 4:
                    break

                else:
                    print('\033[31mERRO!! Digite um dos valores no menu.\033[m')
        else:
            print('\033[31mUsuario não cadastrado\033[m')
    elif opc == 4:
        break
    else:
        print('\033[31mERRO!! Digite um dos valores no menu.\033[m')
        
print('VOLTE SEMPRE!')
