sabores = ["mussarela", "calabresa", "peperoni", "quatro queijos", "frango com catupiry"]

sabor = ""
pedido = []

print("Faça seu pedido ou digite 'sair' para encerrar: ")

while(sabor.lower() != "sair"):
    sabor = input("Escolha o sabor da sua pizza: ")
    
    if sabor in sabores:
        pedido.append(sabor)
        print(f" {sabor} adicionado ao pedido")
    elif sabor.lower() == 'sair':
        print ("Pedido encerrado")
    else:
        print("Esse sabor não está no cardápio, Escolha novamente")


print(pedido)