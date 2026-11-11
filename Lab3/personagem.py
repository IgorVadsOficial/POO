"""Módulo Personagem — versão base para o Lab 3.

👉 Este arquivo deve conter sua implementação completa dos Labs 1 e 2.
   Cole aqui os métodos que você implementou antes de prosseguir.
"""

from dado import rolar_todos_atributos
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class Personagem:
    """Representa um herói genérico no mundo de Forja de Heróis."""

    def __init__(self, nome: str, rolar: bool = True):
        
        self.nome = nome
        if rolar:
            atributos = rolar_todos_atributos()
            self.forca = atributos["FOR"]
            self.destreza = atributos["DES"]
            self.constituicao = atributos["CON"]
            self.sabedoria = atributos["SAB"]
            self.inteligencia = atributos["INT"]
            self.carisma = atributos["CAR"]
        else:
            self.forca = 0
            self.destreza = 0
            self.constituicao = 0
            self.sabedoria = 0
            self.inteligencia = 0
            self.carisma = 0


    def nivel_total(self) -> int:
        return (
            self.forca + self.destreza + self.constituicao
            + self.sabedoria + self.inteligencia + self.carisma
        )

    def __str__(self) -> str:
        return f"{self.nome} (nível total: {self.nivel_total()})"

    def __repr__(self) -> str:
        return f"Personagem('{self.nome}', rolar=False)"

    def __eq__(self, other) -> bool:
        return self.nivel_total() == other.nivel_total()


    def __lt__(self, other) -> bool:
        return self.nivel_total() < other.nivel_total()

    def exibir_ficha_rich(self) -> None:
        from rich.console import Console
        from rich.table import Table
        from rich.panel import Panel

        console = Console()
        tabela = Table(title=f"Ficha de {self.nome}")
        tabela.add_column("Atributo")
        tabela.add_column("Valor", justify="right")
        for nome, val in [
            ("FOR", self.forca),
            ("DES", self.destreza),
            ("CON", self.constituicao),
            ("SAB", self.sabedoria),
            ("INT", self.inteligencia),
            ("CAR", self.carisma),
        ]:
            tabela.add_row(nome, str(val))
        console.print(Panel(tabela))

