saldo = 500 #Saldo inicial do usurário

while saldo > 0: # O laço do while continuará a ser executado até que o saldo acabe
    print(f" \nSaldo Disponivel: {saldo:.2f}")
    saque = input("Digite o valor para sacar ou 'sair' para encerrar: ")

    if saque.lower() == 'sair':
        print("Operação encerrada")
        break

    saque = float(saque)

    if (saque > saldo):
        print("⚠Saldo insuficiente!⚠")
    else:
        print(f'Saque de R${saque:.2f} realizado')
        saldo -= saque #operação de decremento e reatribuição ao mesmo tempo.