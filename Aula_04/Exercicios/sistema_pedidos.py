# Cardápio da Pizzaria
cardapio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90,

}


#Pedido inicial do cliente
pedido = []

pedido.append("mussarela")
pedido.append("calabresa")

total = sum(cardapio[sabor] for sabor in pedido)

#print(f"O total é:{total:.2f}")

# Resumo do Pedido

print(f""" 👌Resumo do Pedido""")

for sabor in pedido:
      print(f"🍕 - {sabor}: R${cardapio[sabor]:.2f}")

print(f"💸O total é: R${total:.2f}")


