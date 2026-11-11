class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    # ---------- properties ----------
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome

    @property
    def cpf(self):
        return self._cpf

    # Sem setter para cpf: o documento não deve mudar depois de criado.

    # ---------- métodos ----------
    def nome_completo(self):
        return "{} {}".format(self._nome, self._sobrenome)

    def __str__(self):
        return "{} (CPF: {})".format(self.nome_completo(), self._cpf)


if __name__ == "__main__":
    from conta import Conta

    cliente1 = Cliente("João", "Silva", "111.111.111-11")
    cliente2 = Cliente("Maria", "Souza", "222.222.222-22")

    conta1 = Conta("123-4", cliente1, 1200.0, 1000.0)
    conta2 = Conta("567-8", cliente2, 500.0, 1000.0)

    # O titular agora é um objeto Cliente, não mais uma string
    print(conta1.titular.nome_completo())
    print(conta2.titular)

    conta1.transfere_para(conta2, 200.0)
    conta1.extrato()
    conta2.extrato()

    # Alterando o nome do cliente: reflete na conta
    cliente1.sobrenome = "Santos"
    print(conta1.titular.nome_completo())
