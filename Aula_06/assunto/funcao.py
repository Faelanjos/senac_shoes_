# Sintaxe básica de uma função


def nome_da_função():
    # codigo da função
    return




# Função sem paramentros e sem retorno
def ola_mundo():
    print("Ola mundo")

ola_mundo()

# Função com paramentros e sem retorno
def saudacao(nome):
    print(f"Ola, seja bem vindo {nome}")

saudacao("Rafael")

# Função com paramentros e com retorno
def soma(a, b):
    total = a + b
    return total