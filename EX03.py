class Veiculo:
    def __init__(self, capacidade_total, combustivel_presente):
        self.__capacidade_total = capacidade_total
        self.__combustivel_presente = combustivel_presente

    def get_capacidade_total(self):
        return self.__capacidade_total

    def get_combustivel_presente(self):
        return self.__combustivel_presente

    def set_capacidade_total(self, capacidade):
        self.__capacidade_total = capacidade

    def set_combustivel_presente(self, combustivel):
        self.__combustivel_presente = combustivel

    def abastecer(self, litro):
        if (
            self.get_combustivel_presente() < self.get_capacidade_total()
            and self.pode_abastecer(litro) == True
        ):
            self.__combustivel_presente += litro
        else:
            print("Tanque está cheio!")

    def pode_abastecer(self, quantidade):
        if (
            self.get_combustivel_presente() < self.get_capacidade_total()
            and (self.get_combustivel_presente() + quantidade)
            <= self.get_capacidade_total()
        ):
            return True
        else:
            return False


class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__valorLitro = valorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel

        if self.__tipoCombustivel == 1:
            nome_tipo = "Gasolina"
        elif self.__tipoCombustivel == 2:
            nome_tipo = "Etanol"
        elif self.__tipoCombustivel == 3:
            nome_tipo = "Diesel"

        print(f"Combustivel definido como: {nome_tipo}")

    def get_tipoCombustivel(self):
        return self.__tipoCombustivel

    def get_valorLitro(self):
        return self.__valorLitro

    def get_quantidadeCombustivel(self):
        return self.__quantidadeCombustivel

    def set_tipoCombustivel(self, tipo):
        self.__tipoCombustivel = tipo

    def set_valorLitro(self, valor):
        self.__valorLitro = valor

    def set_quantidadeCombustivel(self, quantidade):
        self.__quantidadeCombustivel = quantidade

    def abastecerPorValor(self, valor, carro):
        litro = valor / self.get_valorLitro()
        if valor >= self.get_valorLitro() and carro.pode_abastecer(litro) == True:
            carro.abastecer(litro)
            self.set_quantidadeCombustivel(self.get_quantidadeCombustivel() - litro)
            print(f"Foram colocados {litro}L no carro!")
        else:
            print("Valor insuficiente!")

    def abastecerPorLitro(self, quantidade, carro):
        valor = quantidade * self.get_valorLitro()
        litro = valor / self.get_valorLitro()
        if (
            quantidade > 0
            and self.get_quantidadeCombustivel() >= quantidade
            and carro.pode_abastecer(litro) == True
        ):
            self.set_quantidadeCombustivel(self.get_quantidadeCombustivel() - litro)
            carro.abastecer(litro)
            print(f"Valor a pagar R${valor:.2f}")
        else:
            print("Impossivel colocar essa quantidade.")

    def alterarValor(self, valor):
        self.set_valorLitro(valor)

    def alterarCombustivel(self, tipo):
        self.set_tipoCombustivel(tipo)

        if self.get_tipoCombustivel() == 1:
            nome_tipo = "Gasolina"
        elif self.get_tipoCombustivel() == 2:
            nome_tipo = "Etanol"
        elif self.get_tipoCombustivel() == 3:
            nome_tipo = "Diesel"
        else:
            nome_tipo = "Desconhecido"

        print(f"Combustivel alterado para: {nome_tipo}")

    def alterarQuantidadeCombustivel(self, quantidade):
        self.set_quantidadeCombustivel(quantidade)


bomba = BombaCombustivel(
    int(
        input(
            "--Bomba--\nDigite: \n 1 - Gasolina \n 2 - Etanol \n 3 - Diesel \nTipo: \n"
        )
    ),
    float(input("Valor do litro: R$")),
    float(input("Quantidade de combustivel na bomba [L]: ")),
)

carro = Veiculo(
    float(input("\n--Carro--\nCapacidade máxima do tanque [L]: ")),
    float(input(f"Quantidade de combustivel no carro [L]: ")),
)

valor_desejado = float(input("Valor que deseja abastercer: R$"))
bomba.abastecerPorValor(valor_desejado, carro)

litros_desejado = float(input("Quando litros deseja abastercer [L]: "))
bomba.abastecerPorLitro(litros_desejado, carro)

valor = float(input("Novo valor: R$"))
bomba.alterarValor(valor)

tipo = int(
    input(
        "Para alter combustivel digite: \n 1 - Gasolina \n 2 - Etanol \n 3 - Diesel \nTipo: "
    )
)
bomba.alterarCombustivel(tipo)

quantidade = float(input("Nova quantidade na bomba: "))
bomba.alterarQuantidadeCombustivel(quantidade)
