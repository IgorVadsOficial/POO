from conta import Conta, ContaCorrente, SeguroDeVida, TributavelMixIn

# Compatibilidade com os exercícios que ainda importam o nome antigo.
Tributavel = TributavelMixIn


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, limite, valor):
        super().__init__(numero, titular, saldo, limite)
        self.valor = valor
