# Calabresa, 4 Queijos, Frango com Requeijão

# Se o cliente pedir uma pizza de Calabresa na sexta-feira, o refrigerante é de graça;

# Se o cliente pedir qualquer pizza no sabado o frete é grátis, 

# Senão informe ao cliente que a pizza solicitada está sendo preparada.


sabor_pizza = eval(input(f"""
                    ========+🍕PIZZARIA SABORES🍕+=========
                    Digite o sabor que você deseja: 
                    1 - Calabresa
                    2 - 4 queijos
                    3 - Frango com Requeijão
                    : """))
dia_semana = "sabado"


if(sabor_pizza == 1 and dia_semana == "sexta"):
    print("✅Parabéns, você ganhou um refrigente✅")
elif((sabor_pizza == 1 or sabor_pizza == 2 or sabor_pizza == 3) and (dia_semana == "sabado")):
    print("✅Parabéns, seu frete é por nossa conta✅")
else:
    print("Sua 🍕está sendo preparada ")

