# Aula 01

## Nomeclatura
- Um ``arquivo`` .py em python, chamamos de módulo.
- Uma ``pasta`` dentro do Workspace, chamamos de diretório.

1. Cases:
``snake_case`` separa as palavras por underline, sempre com letras minusculas.

``camelCase`` inicia com letra minuscula, e caso haja uma nova palavra, a primeira letra dela fica maiúscula.

## Observações
1. Python é uma linguagem fracamente tipada.


# Aula 02
1. Para informar quantas casas decimais você quer após a virgula, utilizamos o comando :.xf, sendo o x o número de casas que desejamos exibir.

2. Ao dividirmos 2 numeros inteiros, caso seja necessário, ocorre uma conversão implicita.


# Aula 03
1. Em python, no momento que vamos realizar alguma operação, existe uma precedencia. Como na matematica. Multiplicação e divisão, depois soma e subtração.
Podemos utilizar as ``()`` para mudar a ordem de precedencia.

2. Toda vez que utilizamos o metodo ``input()``, por padrão ele nos devolve uma ``string``.

3. Para converter uma string para ``int`` ou ``float``, podemos utilizar os metodos ``int()`` ou ``float()``

# Aula 05
## Estruturas de repetição:
1. ``for``
=> utilizado quando de antemão, se sabe quantas repetições são necessárias. Normalmente é utilizado para ``iterar`` sobre elementos de uma sequência 
1.1 - range() => Gera uma sequencia de números (1º sendo inclusivo e ultimo é exclusivo)

2. ``while``
=> utiizado quando não se sabe quantas vezes a repetição ocorreá ao certo. Será executado enquanto a condição for verdadeira.

# Aula 06
## Comandos de Desvio
1. continue -> Siginifica continuar, basicamente se uma condição for favoravel, ela será desconsiderada.

2. break -> Significa quebrar, quando utilizado irá finalizar o loop mais próximo.

## Funções
=> Bloco de código que é reutilizável, serve para deixa o c´doigo mais organizado e eficiente. ``Executam uma tarefa especifica.``

# Aula 07
## Principios da programação orientada a objetos (P.O.O):
1. ``Encapsulamento``
2. ``Herança`` => é um conceito de POO que permite que uma classe herde atributos e métodos de outras classes
3. ``Polimorfismo``
4. ``Abstração``

## Palavras Reservadas em POO
1. ``class`` => é uma palavra chave em python onde você cria um 'molde'. Toda classe pode classe pode ter 'atributos' e 'metodos', sendo que os atributos precisam estar dentro de um metodo chamado construtor(__init__).
2. ``object`` => é o nome dado a cada cópia da classe. Também conhecido como instância.
3. ``__init__`` => é um inicializador (construtor), onde você informa que toda cópia precisa passar aqueles valores no momento da criação. É um método especial.
4. ``this / self`` => referencia o atributo atual da classe(valor). Em outras linguagens se usa o o this, porém em python se usa o self.

## Termos utilizados em POO
1. ``metodo`` => é uma função que está dentro de uma classe. É uma ação.
2. ``atributos`` => são as caracteristicas de uma classe.

## Herança
Teremos dois tipos de classes:
- superclass => é a classe pai, que oferece a herança.
- subclass => é a classe filha, que herda a herança.

## Atalhos no Vscode
``CTRL + B`` => Oculta ou exibe o explorador.
``CTRL + ;`` => Comenta uma linha.
``SHIFT + Alt + ↑ ou ↓`` => Duplica uma linha para cima ou para baixo.
``CRTL + ASPAS`` = Oculta o exibe o terminal.
``CTRL + D`` = Seleciona a proxima ocorrência
``WINDOWS + Ç`` = Exibe emoji