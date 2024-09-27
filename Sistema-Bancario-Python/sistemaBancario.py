saldo = 0

continuar = 's'

movimentacoes = []

while continuar == "s":
    deposito = float(input("Digite o valor do depósito: "))
    saldo += deposito
    if deposito > 0:
        movimentacoes.append(deposito)
    continuar = input("Deseja fazer um novo deposito? (s/n) ")
    

continuar = 's'
nsaq = 0

while continuar == "s":
    if nsaq < 3:
        saque = float(input("Digite o valor do saque: "))
        if saque <= saldo:
            if saque <= 500:
                if saque > 0:
                    movimentacoes.append(-saque)
                saldo -= saque
                continuar = input("Deseja fazer um novo saque? (s/n) ")
            else:
                print("O valor solicitado é maior que o permitido")
                continuar = input("Deseja fazer um novo saque? (s/n) ")
            nsaq += 1
        else:
            print("Saldo insuficiente")
            continuar = input("Deseja fazer um novo saque? (s/n) ")
    else:
        break
    

continuar = 's'

if not movimentacoes:
    print("Não foram realizadas movimentações.")
else:
    print("- - Extrato - -")
    for i in movimentacoes:
        if i > 0:
            print(f'Depósito - - - (+)R${i:.2f}')
        else:
            print(f'Saque    - - - (-)R${-i:.2f}')
    print(f'Saldo Final - - - R${saldo:.2f}')