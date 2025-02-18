#Calculo de frete

distancia_cliente = float(input("Para calculo de frete, digite a distancia da sua casa: "))
taxa_fixa = 5
valor_frete = 0
valor_perto = 1
valor_longe = 2


if(distancia_cliente <= 5):
    valor_frete = (distancia_cliente*valor_perto) + taxa_fixa
    print(f"O valor do seu frete é de {valor_frete} reais")
elif(distancia_cliente <= 10):
    valor_frete = (distancia_cliente*valor_longe) + taxa_fixa
    print(f"O valor do seu frete é de {valor_frete} reais")
else:
    print("Lamentamos informar mas não fazemos entrega no seu endereço")

