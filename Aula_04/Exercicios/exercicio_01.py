#Crie uma lista de sabores de pizzas pedidos pelo cliente. Adicione 3 sabores à lista e remova 1 sabor. Exiba o pedido final.

cardapio = {
    "mussarela":25.90,
    "calabresa":27.90,
    "frango com catupiry":29.90,
    "portuguesa": 31.90
}

pedido = []
continua = True

print(f"""
      📖Segue o cardápio📖   
      """)
for sabor,preco in cardapio.items():
    print(f"\n{sabor} custa R$ {preco:.2f}")

while(continua):
    pedido.append(input("Digite o sabor da pizza: "))
    continua = input("Deseja pedir algo mais? S ou N ")
    if (continua == "S"):
        continua = True
    else:
        continua = False


total = sum(cardapio[sabor] for sabor in pedido)


print(f""" 👌Resumo do Pedido""")

for sabor in pedido:
      print(f"🍕 - {sabor}: R${cardapio[sabor]:.2f}")

print(f"💸O total é: R${total:.2f}")
