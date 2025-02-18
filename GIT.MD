# Passo a passo para utlização básica do Git/GitHub

1. Ir no GitHub e criar o repository dos arquivos que você quer enviar.
2. Abrir o diretório do projeto no VScode.
3. Abrir a tela do terminal do VScode (CRTL+J)
4. git init -> Cria o repositório local do projeto na pasta onde ele está armazenado.
5. Informar as credencias do GIT. Isso é realizado apenas uma única vez no computador:
    git config --global user.name "Seu Nome"
    git config --global user.email "seu_email@example.com"
6. git status -> Verifica quais arquivos/pastas foram enviadas para o repositório local.
7. git add . -> Inclui todos os arquivos/pastas no repositório local
8. git branch -M main -> Altera o nome da branch atual para main.
9. git commit -m "A informação fica aqui" -> Realiza um novo commit no repositório local.
10. git remote add origin endereço_do_repositório_remoto -> Comando para realizar a sincronização do repositório local com o remoto.
11. git push -u origin main -> envia o repositório local para o remoto.
