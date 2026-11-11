class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for tributavel in lista_tributaveis:
            total += tributavel.get_valor_imposto()
        return total


if __name__ == "__main__":
    from conta import ContaCorrente, SeguroDeVida, TributavelMixIn

    cc1 = ContaCorrente("123-4", "João", 1000.0)
    cc2 = ContaCorrente("123-4", "José", 1000.0)
    seguro1 = SeguroDeVida(100.0, "José", "345-77")
    seguro2 = SeguroDeVida(200.0, "Maria", "237-98")

    lista_tributaveis = [cc1, cc2, seguro1, seguro2]
    assert all(isinstance(item, TributavelMixIn) for item in lista_tributaveis)

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)
    print(total)
