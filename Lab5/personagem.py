"""Módulo Personagem — Lab 4: adiciona atacar() e pontos_de_vida.

👉 Cole aqui sua implementação completa dos Labs 1–3 e acrescente
   os métodos novos abaixo (esta versão já os fornece prontos).
"""

from dado import rolar_todos_atributos
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


class Personagem:
    """Representa um herói no mundo de Forja de Heróis."""

    def __init__(self, nome: str, rolar: bool = True):
        self.nome = nome
        self.pontos_de_vida = 100
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
        
    # --- Métodos novos — já fornecidos ---

    def esta_vivo(self) -> bool:
        """Retorna True se o personagem ainda tem pontos de vida."""
        return self.pontos_de_vida > 0

    def receber_dano(self, dano: int) -> None:
        """Reduz os pontos de vida pelo dano recebido (mínimo 0)."""
        self.pontos_de_vida = max(0, self.pontos_de_vida - dano)

    def atacar(self, alvo: "Personagem") -> int:
        """Ataca outro personagem — deve ser sobrescrito pelas subclasses."""
        raise NotImplementedError(
            f"{type(self).__name__} deve implementar o método atacar()."
        )

    def __str__(self) -> str:
        return f"{self.nome} [{type(self).__name__}] PV:{self.pontos_de_vida}"

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
        
