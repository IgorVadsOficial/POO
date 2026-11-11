# Etapa 1.

# Observe o erro gerado e explique por que não é possível acessar o atributo privado diretamente.
"""Foi gerado um erro informando que o objeto Banco não tem um atributo chamado "__nome". Não é possivel acessar diretamente
porque foi utilizado os dois underscores e tornou o atributo como privado."""

# Por que o Python utiliza dois underscores para indicar atributos privados e como isso afeta o acesso aos atributos?
"""Python utiliza dois underscores (__) para implementar o name mangling ou deformação de nome que é um 
mecanismo do Python que renomeia automaticamente atributos com dois underscores (__) quando estão dentro de uma classe."""


class Banco:
    def __init__(self, nome):
        self.__nome = nome


meu_banco = Banco("Banco Central")

print(meu_banco.__nome)

# Etapa 2.

# Explique por que agora é possível acessar o atributo privado através do método público.
"""Porque foi criado um método que retorna o valor de "__nome" tornando um atributo que era privado em um público."""

# Qual é a importância de usar métodos públicos para acessar atributos privados em termos de encapsulamento?
"""Usar métodos públicos para acessar atributos privados é importante pelos seguintes motivos: Validação de dados, por exemplo no set você 
poderia garantir que o set_idade pudesse aceitar apenas valores que sejam maiores que zero; Fácil manutenção, se você quissesse modificar
a forma por exemplo de como o get_preco mostrava os preços em um site era só modificar esse metódo e iria modificar em todo o código."""


class Banco:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome


meu_banco = Banco("Banco Central")

print(meu_banco.get_nome())

# Etapa 3.

# Explique como o método setter permite controlar a modificação de atributos privados.
""""""

# Quais são as vantagens de controlar o acesso e modificação de atributos privados através de métodos públicos?
""""""


class Banco:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome


meu_banco = Banco("Banco Central")

meu_banco.set_nome("Banco Nacional")

print(meu_banco.get_nome())

# Etapa 4.

# Explique por que é importante realizar validações ao modificar atributos.
""""""

# Como as validações nos setters contribuem para a integridade dos dados em uma classe?
""""""


class Banco:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if len(novo_nome) >= 3:
            self.__nome = novo_nome
        else:
            print("Nome inválido. Deve ter pelo menos 3 caracteres.")


meu_banco = Banco("Banco Central")

meu_banco.set_nome("Banco Nacional")

print(meu_banco.get_nome())

# Etapa 5.
