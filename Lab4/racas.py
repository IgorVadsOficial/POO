"""Módulo de raças — Lab 4: cada subclasse implementa atacar() de forma diferente.

Isso é polimorfismo: a Arena chama atacante.atacar(alvo) sem saber qual subclasse é.
"""

from personagem import Personagem
from dado import rolar_dado


class Guerreiro(Personagem):
    """Guerreiro: ataque físico baseado em FOR."""

    bonus_racial = {"forca": 2, "constituicao": 1}

    def __init__(self, nome: str, rolar: bool = True):
        super().__init__(nome, rolar)
        for atributo, valor in self.bonus_racial.items():
            setattr(self, atributo, getattr(self, atributo) + valor)

    # ------------------------------------------------------------------
    # TODO 4-A: implemente atacar() para o Guerreiro.
    #
    # Regra de dano:
    #   modificador = (self.forca - 10) // 2
    #   dano = rolar_dado(8) + modificador
    #
    # O método deve:
    #   1. Calcular o dano
    #   2. Chamar alvo.receber_dano(dano)
    #   3. Imprimir uma mensagem, ex:
    #      "⚔  Arador golpeia Elara com 9 de dano físico!"
    #   4. Retornar o dano (int)
    # ------------------------------------------------------------------
    def atacar(self, alvo: Personagem) -> int:
        modificador = (self.forca - 10) // 2
        dano = rolar_dado(8) + modificador
        alvo.receber_dano(dano)
        print(f"⚔  {self.nome} golpeia {alvo.nome} com {dano} de dano físico!")
        return dano


class Mago(Personagem):
    """Mago: ataque mágico baseado em INT."""

    bonus_racial = {"inteligencia": 2, "sabedoria": 1}

    def __init__(self, nome: str, rolar: bool = True):
        super().__init__(nome, rolar)
        for atributo, valor in self.bonus_racial.items():
            setattr(self, atributo, getattr(self, atributo) + valor)

    # ------------------------------------------------------------------
    # TODO 4-B: implemente atacar() para o Mago.
    def atacar(self, alvo: Personagem) -> int:
        modificador = (self.inteligencia - 10) // 2
        dano = rolar_dado(6) + rolar_dado(6) + modificador
        alvo.receber_dano(dano)
        print(f"✨ {self.nome} lança magia em {alvo.nome} causando {dano} de dano mágico!")
        return dano
    # ------------------------------------------------------------------
