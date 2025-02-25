#Pessoa, Professor, Aluno

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def exibir_dados(self):
        return f'Nome:{self.nome} | Idade: {self.idade} | CPF: {self.cpf}'

#Criando a subclass Aluno
class Aluno(Pessoa):
    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf) #herda os atributos da class Pessoa
        self.matricula = matricula
        self.notas = [] #Lista para armazenar as notas do Aluno
    
    def adicionar_notas(self, nota):
        self.notas.append(nota)

    def calc_media(self):
        return sum(self.notas) / len(self.notas)
    
    def exibir_dados(self):
        return f'{super().exibir_dados()} | Matricula: {self.matricula}'




class Professor(Pessoa):
    def __init__(self, nome, idade, cpf, disciplina, salario):
        super().__init__(nome, idade, cpf)
        self.disciplina = disciplina
        self.salario = salario
    
    def exibir_dados(self):
        return f'''{super().exibir_dados()} | Salario: R${self.salario:.2f} | Disciplina: {self.disciplina}'''



aluno1 = Aluno("Rafael", 34, "12529765774", "2010100784")

professor1 = Professor("Carlos Mendes", 48, "12345678971", "Matematica", 50000)

#Exibindo as informações

print(aluno1.exibir_dados())

print(professor1.exibir_dados())