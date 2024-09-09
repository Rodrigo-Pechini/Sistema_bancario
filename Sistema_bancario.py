menu = f"""
{'=' * 20}
        MENU
    [1] Depositar
    [2] Retirar
    [3] Extrato
    [4] Sair
{'=' * 20}
    """

saques = 0
extrato = []
saldo_total = 0
operacoes = {}

while True:
    
    print(menu)
    opc = int(input('Digite uma das opções: '))

    #Filtra a opção do usuario
    if opc in (1, 2, 3, 4):

        #Depositando um valor no saldo total e no deposito
        if opc == 1:
            deposito = int(input('Deposito de R$'))
            if deposito > 0:
                print(f'\033[32mDeposito de R${deposito} foi efetuado\033[m')
                saldo_total += deposito
                operacoes['deposito'] = deposito

                #adiciona uma copia do dicionario(operacoes) na lista(extrato)
                extrato.append(operacoes.copy())
                operacoes.clear()
            else:
                print('Digite um valor valido para deposito')
        
        #Retirando um valor do saldo_total
        elif opc == 2:
            retirar = int(input('Retirada de R$'))

            if retirar < saldo_total and retirar <= 500 and saques < 3:
                saldo_total -= retirar
                operacoes['saque'] = retirar
                print(f'\033[31mSaque de R${retirar} foi efetuado\033[m')

                #adiciona uma copia do dicionario(operacoes) na lista(extrato)
                extrato.append(operacoes.copy())
                operacoes.clear()
                saques += 1
            else:
                if retirar > 500 and saques < 3:
                    print('\033[31mErro!! O maximo que se pode retirar é R$500\033[m')
                elif retirar <= 500 and saques == 3:
                    print('\033[31mErro!! O limite de saques diarios foi atingido\033[m')
                else:
                    print('\033[31mErro!! Saldo insuficiente.\033[m')
                
        #Exibindo o extrato do ultimo deposito e o ultimo saque
        elif opc == 3:
            if len(extrato) > 0:

                #Percorre a lista com os dicionarios
                for dic in extrato:

                    #percorre os totos o items do dicionario e printa
                    for val in dic.items():
                        print(f'{val[0]} = {val[1]:.2f}')
            else:
                print('Nenhuma operação foi feita.')
            print(f'saldo: R${saldo_total:.2f}')

        #sair do programa/banco
        else:
            break

    else:
        print('ERRO! Digite uma das opções!')

print('VOLTE SEMPRE!')
