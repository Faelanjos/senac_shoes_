#Crie um dicionário para o cardápio e adicione um novo sabor com preço. Atualize o preço de um sabor existente e remova um sabor do cardápio.

cardapio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90,

}

# Adcionando um sabor
cardapio["portuguesa"] = 30.90


# Alterando um o preço de um sabor
cardapio["mussarela"] = 24.90

# Removendo um sabor do cardápio
cardapio.pop("calabresa")

print(cardapio)
