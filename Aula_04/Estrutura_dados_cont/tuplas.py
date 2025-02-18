"""
As Tuplas são coleções ordenadas, porém são imutáveis.
Podem ser homogêneas ou heterogênas
"""
# Declaração das tuplas
tamanhos = ("broto", "média", "grande")

print(f"""

    🤳Tamanhos disponíveis {tamanhos}

""")


# Operações com tuplas
# Acessar itens
print(tamanhos[2])

# Verificar itens
print("✅ Existe tamanho grande?", "grande" in tamanhos)
