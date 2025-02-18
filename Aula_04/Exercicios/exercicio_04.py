#Crie um dicionário com os estoques de cada sabor. Decremente o estoque conforme os pedidos feitos e exiba uma mensagem se o estoque acabar.

cardapio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90,
}

estoque = {
    "mussarela": 10,
    "calabresa": 10,
    "frango com catupiry": 10,
}

#Pedido inicial do cliente
pedido = []

pedido.append("mussarela")
pedido.append("calabresa")

for sabor in pedido:
    estoque[sabor] = estoque[sabor]-1

print(estoque)