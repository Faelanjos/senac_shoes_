#aluno -> nome, idade, endereço, cpf.

class Aluno: # utilizamos o padrão PascalCase para as classes.
    def __init__(self, nome, idade, endereco, cpf):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.matriculado = True


    # Método que altera o status da matricula do aluno
    def situacao(self):
        if (self.matriculado == True):
            self.matriculado = False
        else:
            self.matriculado = True

    #Metodo que exibe as informações do aluno
    def exibir_info(self):
        return( f''' 
        DADOS DO ESTUDANTE
        O nome do aluno é {self.nome} 
        tem {self.idade} anos,
        mora na {self.endereco}''')
        

# criando cópias da calsse Aluno(instânciação)
a1 = Aluno("Rafael", 34, "Rua Barao de Guaratiba", "12529765774")
a2 = Aluno("Ana", 22, "Rua Barao de Guaratiba", "12345678912")

print(a1.exibir_info())
