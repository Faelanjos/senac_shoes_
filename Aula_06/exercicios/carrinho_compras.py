# Crie um programa que permita adicionar produtos a um carrinho de compras. O programa deve continuar pedindo produtos até que o usuário digite "finalizar". No final, exiba todos os produtos comprados.

produtos = ['sabão', 'veja', 'detergente', 'arroz', 'feijão', 'macarrão', 'ovos', 'carne', 'frango']
pedido = []

itens = input("Digite o item que deseja adcionar no seu pedido, ou 'finalizar' para encerrar: ")


while (itens.lower() != 'finalizar'):
    
    if itens in produtos:
        pedido.append(itens)
        print(f"✅O item {itens} foi adicionado ao seu pedido")
    else:
        print('⚠ O item escolhido não está na lista')
    
    itens = input("Digite o item se deseja adicionar algo mais, ou 'finalizar' para encerrar: ")

if len(pedido) > 0: 
    print('''Segue seu pedido''')
    for item in pedido:
        print(f'◽{item}')
else:
    print('\nCarrinho vazio')
