nome = input('Seu nome completo: ')
idade = int(input('Sua idade: '))
saldo = float(input('Seu Saldo: '))
saldo2 = saldo  # saldo2 exite para que as informações do saldo sejam atualizadas sem entrar em conflito
nome = nome.upper()  # Essa linha deixa o nome em caixa alta, pois o nome do cliente deve ser sempre valorizado.


def fsaque(nome, idade, saldo):
    global saldo2    # essa linha deixa o saldo2 global e permite a atualização de seus valores
    print(f"""
    SAQUE
    """)
    valor_saque = float(input(f"""Digite o valor o valor desejado para saque:  """))
    if (valor_saque > 1000) or (valor_saque >= float(saldo)):
        print(f"""Saque indiponível, valor indisponível ou acima de R$1000,00""")

    else:
        saldo_atual = saldo2 - valor_saque
        print(f"""
        SAQUE REALIZADO
        """)
        print(f"""
        SALDO ATUAL É DE {saldo_atual}
        """)
        saldo2 = saldo_atual

    return opcoes(nome, idade, saldo)


def fdeposito(nome, idade, saldo):
    global saldo2
    valor_deposito = float(input(f"""
    Qual valor desejado para o depósito: """))
    if valor_deposito >= 5000:
        print(f"""
        Seu valor foi recusado 
        """)
    else:
        saldo_atual = saldo2 + valor_deposito
        print(f"""
        seu valor de depósito foi aprovado
        """)
        print(f"""
        SALDO ATUAL É DE {saldo_atual}
        """)
        saldo2 = saldo_atual

    return opcoes(nome, idade, saldo)


def femprestimo(nome, idade, saldo):
    global saldo2, saldo_atual
    valor_emprestimo = float(input(f"""
    Qual o valor desejado para empréstimo?  """))
    max_emprestimo = saldo2 * 15
    if idade >= 21:
        if saldo >= 1000 and 2000 <= valor_emprestimo <= max_emprestimo:
            print(f"""
            EMPRÉSTIMO ACEITO
            """)
            saldo_atual = saldo2 + valor_emprestimo
            print(f"""
            SALDO ATUAL É DE {saldo_atual}
            """)
            saldo2 = saldo_atual
    else:
        print(f"""
        Nessesária idade mínima de 21 anos
        """)
    saldo = saldo_atual
    return opcoes(nome, idade, saldo)


def saldo_atual(args):
    pass


def finfo(nome, idade):
    global saldo2
    print(f"""
    {nome}, obrigado por escolher nossos serviços,
    Atualmente com {idade} anos,
    você tem R$ {saldo2} em sua conta.
    """)
    return opcoes(nome, idade, saldo)


def opcoes(nome, idade, saldo):
    print('Digite (1) para saque')
    print('Digite (2) para depósito')
    print('Digite (3) para empréstimo')
    print('Digite (4) para visualizar informações')
    print('Digite (Qualquer outro texto ou número) para sair')

    menu = input(f"""
    Digite aqui: """)

    if menu == '1':
        fsaque(nome, idade, saldo)

    elif menu == '2':
        fdeposito(nome, idade, saldo)

    elif menu == '3':
        femprestimo(nome, idade, saldo)

    elif menu == '4':
        finfo(nome, idade)


if saldo:
    opcoes(nome, idade, saldo)
