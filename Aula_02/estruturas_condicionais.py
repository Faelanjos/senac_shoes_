idadePessoa = 0
valida = True



# while(valida):
#     idadePessoa = int(input("Digite sua idade: "))
#     if(idadePessoa >= 18):
#         print("Pode dirigir")
#         valida = False
#     elif(idadePessoa >= 0 and idadePessoa<= 17):
#         print("Não pode dirigir")
#         valida = False
#     else:
#         print("Informe uma idade válida")


idade = 17
habilitacao = False

if (idade >= 18):
    if (habilitacao):
        print("Você já pode dirigir")
    else:
        print("Você não possui habilitação.")
else:
    print("Você não tem idade suficiente para dirigir")