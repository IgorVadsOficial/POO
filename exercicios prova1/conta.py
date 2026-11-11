class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    # ---------- properties ----------
    @property
    def numero(self):
        return self._numero

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    # Não há setter para saldo: o saldo só deve mudar por meio de
    # deposita(), saca() e transfere_para().

    # ---------- métodos ----------
    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if self._saldo < valor:
            return False
        self._saldo -= valor
        return True

    def extrato(self):
        print("numero: {}\nsaldo: {}".format(self._numero, self._saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        destino.deposita(valor)
        return True


class TributavelMixIn:
    def get_valor_imposto(self):
        raise NotImplementedError


class ContaCorrente(Conta, TributavelMixIn):
    def __init__(self, numero, titular, saldo, limite=1000.0):
        super().__init__(numero, titular, saldo, limite)

    def get_valor_imposto(self):
        return self._saldo * 0.01


class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05


if __name__ == "__main__":
    conta1 = Conta("123-4", "João", 1200.0, 1000.0)
    conta2 = Conta("567-8", "Maria", 500.0, 1000.0)

    print(conta1.titular)

    conta1.deposita(100.0)
    conta1.extrato()

    print(conta1.saca(2000.0))  # False (saldo insuficiente)
    print(conta1.saca(300.0))  # True
    conta1.extrato()

    print(conta1.transfere_para(conta2, 400.0))  # True
    conta1.extrato()
    conta2.extrato()
