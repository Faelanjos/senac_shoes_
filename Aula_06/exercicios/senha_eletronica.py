# Crie um sistema que peça para o usuário digitar uma senha para acessar sua conta bancária. Ele tem apenas 3 tentativas para acertar a senha correta. Se ele errar as 3 vezes, o sistema bloqueia a conta

senha_correta = '1234'
tentativas = 3
senha_usuário = input('Digite a sua senha: ')

if senha_usuário == senha_correta :
    print ('✅Senha correta!')
else:
    while (senha_usuário != senha_correta):
        tentativas -= 1
        if tentativas > 0:
            print(f'''Senha incorreta
            Você tem mais {tentativas} tentativas antes da sua conta ser bloqueada''')
        else:
            print('🚫Conta Bloqueada🚫')
            break

        senha_usuário = input('Digite a sua senha novamente: ')


