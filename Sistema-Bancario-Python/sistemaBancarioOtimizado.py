saldo = 0
continuar = 's'
movimentacoes = []

def executar():
    selecao = input("""Selecione a operação desejada:
                    d - Depósito
                    s - Saque
                    e - Extrato
                    """)
    return selecao

def recvalor():
    valor = float(input('Digite o valor: '))
    return valor

def deposito():
    global saldo
    global movimentacoes
    valor = recvalor()
    saldo += valor
    movimentacoes.append(valor)
    
def saque():
    global saldo
    global movimentacoes
    valor = recvalor()
    if valor <= saldo:
        if valor <= 500:
            saldo -= valor
            if valor > 0:
                movimentacoes.append(-valor)
        else:
            print('O valor solicitado é maior que o permitido.')
    else:
        print('Saldo insuficiente para o saque.')
        
def extrato():
    global saldo
    global movimentacoes
    if not movimentacoes:
        print('Não foram realizadas movimentações.')
    else:
        print('- - Extrato - -')
        print('===========================')
        for i in movimentacoes:
            if i > 0:
                print(f'Depósito - - - (+)R${i:.2f}')
            else:
                print(f'Saque  - - - - (-)R${-i:.2f}')
        print('===========================')
        print(f'Saldo Final - - - R${saldo:.2f}')
        
operacoes = {'d':deposito, 's':saque, 'e':extrato}

while continuar == 's':
    i = executar()
    operacoes[i]()
    continuar = input('Deseja realizar outra operação? (s/n) ')