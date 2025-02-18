'''Pizzaria Sabores
Calabresa, Mussarela, Frango
Grande'''
 
# sabor = "Calabresa" #Declarando a variável e inicializando.
sabor = input("Informe qual sabor da sua pizza: ")
TAMANHO = "Grande"
preco = float(input("digite o preço: "))

print(f""" 
=============================================
      A pizza escolhida é de {sabor},
      a pizza {TAMANHO}
      e o valor é de {preco}.
=============================================
""")

