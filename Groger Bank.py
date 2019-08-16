nome = input('Seu nome completo: ')
idade = int(input('Sua idade: '))
saldo = float(input('Seu Saldo: '))



def fsaque():
    print('SAQUE')
    valor_saque = float(input('Digite o valor o valor desejado para saque:'))
    if (valor_saque > 1000) or (valor_saque >= float(saldo)):
        print('Saque indiponível, valor indisponível ou acima de R$1000,00')

    else:
        saldo_atual = saldo - valor_saque
        print('SAQUE REALIZADO')
        print('SALDO ATUAL É DE {}'.format(saldo_atual))

    opcoes()

def fdeposito():
    valor_deposito = float(input('Qual valor desejado para o depósito: '))
    if (valor_deposito >= 5000):
        print('Seu valor foi recusado')
    else:
        saldo_atual = saldo + valor_deposito
        print('seu valor de depósito foi aprovado')
        print('SALDO ATUAL É DE {}'.format(saldo_atual))

    opcoes()

def femprestimo():
    valor_emprestimo = float(input('Qual o valor desejado para empréstimo?  '))
    max_emprestimo = saldo * 15
    if idade >= 21:
        if saldo >= 1000 and 2000 <= valor_emprestimo <= max_emprestimo:
            print('EMPRÉSTIMO ACEITO')
            saldo_atual = saldo + valor_emprestimo
            print('SALDO ATUAL É DE {}'.format(saldo_atual))

    else:
        print('Nessesária idade mínima de 21 anos')

    saldo = saldo_atual
    opcoes()


def finfo():
    print(nome, idade, saldo_atual)


def opcoes():
    print('Digite (1) para saque')
    print('Digite (2) para depósito')
    print('Digite (3) para empréstimo')
    print('Digite (4) para visualizar informações')
    print('Digite (Qualquer outro texto ou número) para sair')

    menu = input('Digite aqui: ')

    if menu == '1':
        fsaque()

    elif menu == '2':
        fdeposito()

    elif menu == '3':
        femprestimo()

    elif menu == '4':
        finfo()


if saldo:
    opcoes()