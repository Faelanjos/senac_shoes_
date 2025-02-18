"""
Os conjuntos não são ordenados, são mutáveis, podem ser homogêneos ou heterogêneos e não permitem elementos duplicados. 

"""

# Declaração dos conjuntos

ingredientes = {"mussarela", "calabresa", "tomate", "azeitona", "tomate"}

print("ingredientes basicos:", ingredientes)

# Operações com os Conjuntos
# Adicionar Itens:
ingredientes.add("oregáno")
print("Ingredientes alualizados:", ingredientes)

# Remover Itens:
ingredientes.remove("tomate")
print("Ingredientes atualizados após a remoção:", ingredientes)

# União de Conjuntos
adicionais = {"bacon", "palmito"}
todos_ingredientes = ingredientes.union(adicionais)

print("Todos os ingredientes:", todos_ingredientes)

# Interseção de Conjuntos: Item aparece em ambos os conjuntos
pizza_vegana = {"tomate", "azeitona", "rucula"}
comuns = ingredientes.intersection(pizza_vegana)

print("Ingredientes comuns:", comuns)
