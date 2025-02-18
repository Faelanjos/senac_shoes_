"""
HOMOGENEO -> Aceita apenas 1 tipo de dado

HETEROGENEO -> Aceita dados de tipos diferentes

As estruturas de dados são declaradas com snake_case ou camelCase.
"""


# Declaração Listas
# Ordenadas, mutáveis e heterogeneas


sabores = ["mussarela", "calabresa", "frango com catupiry", "portuguesa"]

dados_pizza = ["mussarela", 26.90, True]

#print("Sabores disponíveis: ", sabores)
#print("Informações da Pizza: ", dados_pizza)

# Operações com Listas
# 1. append() -> Adiciona um novo valor ao final da lista
sabores.append("margherita")
print("Sabores disponíveis: ", sabores)

# 2. remove() -> Remove um elemento da lista
sabores.remove("calabresa")
print("Sabores disponíveis: ", sabores)

# 3. Para acessar os elementos utilizamos os indices
pizzas = ["mussarela", "calabresa", "frango com catupiry", "portuguesa"]

print(pizzas[0])
print(pizzas[-1])