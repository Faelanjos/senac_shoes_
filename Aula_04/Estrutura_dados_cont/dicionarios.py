"""
Os dicionários podem ser heterogêneos ou homogêneos
São ordenados, mutáveis, e sempre são acompanhados por uma chave:valor

"""

# Declaração de dicionário

cardapio = {
    "mussarela":25.90,
    "calabresa":27.90,
    "frango com catupiry":29.90

}


# print(f"Cardápio da pizzaria sabores:", cardapio)

# Operações com dicionários
#1. Acessar Valores
# print("Preço da pizza de calabresa", cardapio["calabresa"])

#2. Adcionar Valores
cardapio["portuguesa"] = 30.90
# print("Cardapio atualizado:", cardapio)

#3. Alterar Valores
# cardapio["mussarela"] = 26.90
# print("Preço atualizado da pizza de mussarela", cardapio["mussarela"])

#4. Iterar sobre o dicionário
for sabor,preco in cardapio.items():
    print(f"\n A pizza de:{sabor} custa R$ {preco:.2f}")