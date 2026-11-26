from __future__ import annotations


class Produto:
    def __init__(self, codigo: int, nome: str, preco: float):
        self._codigo = codigo
        self._nome = nome
        self._preco = preco

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco

    def __str__(self):
        return f"{self._nome} (R$ {self._preco:.2f})"


class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self._produto = produto
        self._quantidade = quantidade

    @property
    def produto(self):
        return self._produto

    @property
    def quantidade(self):
        return self._quantidade

    @property
    def subtotal(self):
        return self._produto.preco * self._quantidade

    def __str__(self):
        return f"{self._produto.nome} - qtd: {self._quantidade} - subtotal: R$ {self.subtotal:.2f}"


class Pedido:
    def __init__(self, numero: int):
        self._numero = numero
        self._itens = []

    @property
    def numero(self):
        return self._numero

    @property
    def itens(self):
        return self._itens

    def adicionar_item(self, produto: Produto, quantidade: int):
        item = ItemPedido(produto, quantidade)
        self._itens.append(item)

    def remover_item(self, produto: Produto):
        for item in self._itens:
            if item.produto.codigo == produto.codigo:
                self._itens.remove(item)
                return

        raise ValueError("Produto não encontrado no pedido.")

    @property
    def valor_total(self):
        total = 0.0
        for item in self._itens:
            total += item.subtotal
        return total

    def listar_itens(self):
        if not self._itens:
            print("Pedido sem itens.")
            return

        for i, item in enumerate(self._itens, start=1):
            print(f"{i}. {item}")

    def __str__(self):
        return f"Pedido #{self._numero} - Total: R$ {self.valor_total:.2f}"


if __name__ == "__main__":
    teclado = Produto(1, "Teclado mecânico", 250.00)
    mouse = Produto(2, "Mouse gamer", 180.00)
    monitor = Produto(3, "Monitor 27'", 950.00)

    pedido = Pedido(101)
    pedido.adicionar_item(teclado, 1)
    pedido.adicionar_item(mouse, 2)
    pedido.adicionar_item(monitor, 1)

    print("Itens do pedido:")
    pedido.listar_itens()
    print()
    print(pedido)
    print(f"Valor total: R$ {pedido.valor_total:.2f}")
