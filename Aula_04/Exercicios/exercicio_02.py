# Dado dois conjuntos de ingredientes, exiba os ingredientes comuns entre eles e os que estão disponíveis apenas em um conjunto.

ingredientes_1 = {"tomate", "azeite", "ovos"}
ingredientes_2 = {"tomate", "calabresa", "ovos","extrato"}

ingredientes_comuns = ingredientes_1.intersection(ingredientes_2)

ingredientes_unicos = ingredientes_1.symmetric_difference(ingredientes_2)

print(ingredientes_comuns)

print(ingredientes_unicos)
