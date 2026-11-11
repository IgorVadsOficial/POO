"""
Módulo de raças — Lab 5 Desafio.

Guerreiro e Mago já vêm prontos (cole dos labs anteriores ou use as versões abaixo).
Seu trabalho: implementar Arqueiro com atacar() e acerto crítico.
"""

from personagem import Personagem
from dado import rolar_dado
from dado import rolar_todos_atributos


class Guerreiro(Personagem):
    bonus_racial = {"forca": 2, "constituicao": 1}

    def __init__(self, nome: str, rolar: bool = True):
        super().__init__(nome, rolar)
        for atributo, valor in self.bonus_racial.items():
            setattr(self, atributo, getattr(self, atributo) + valor)

    def atacar(self, alvo: Personagem) -> int:
        modificador = (self.forca - 10) // 2
        dano = rolar_dado(8) + modificador
        alvo.receber_dano(dano)
        print(f"⚔  {self.nome} golpeia {alvo.nome} com {dano} de dano físico!")
        return dano
        


class Mago(Personagem):
    bonus_racial = {"inteligencia": 2, "sabedoria": 1}

    def __init__(self, nome: str, rolar: bool = True):
        super().__init__(nome, rolar)
        for atributo, valor in self.bonus_racial.items():
            setattr(self, atributo, getattr(self, atributo) + valor)

    def atacar(self, alvo: Personagem) -> int:
        modificador = (self.inteligencia - 10) // 2
        dano = rolar_dado(6) + rolar_dado(6) + modificador
        alvo.receber_dano(dano)
        print(f"✨ {self.nome} lança magia em {alvo.nome} causando {dano} de dano mágico!")
        return dano

# ------------------------------------------------------------------
# DESAFIO B: implemente a classe Arqueiro.
#
# bonus_racial = {"destreza": 2, "sabedoria": 1}
#
# Regra de atacar():
#   - Role rolar_dado(20). Se >= 18: CRÍTICO → dano = rolar_dado(6) * 2
#   - Caso contrário: dano = rolar_dado(6)
#   - Adicione modificador = (self.destreza - 10) // 2
#   - Chame alvo.receber_dano(dano) e retorne o dano.
#
# Mensagem sugerida:
#   "🏹 Finn dispara em Elara: 7 de dano."
#   "🏹 Finn dispara em Elara: 14 de dano CRÍTICO!"
# ------------------------------------------------------------------
class Arqueiro(Personagem):

    bonus_racial = {"destreza": 2, "sabedoria": 1}

    def __init__(self, nome: str, rolar: bool = True):
        super().__init__(nome, rolar)
        for atributo, valor in self.bonus_racial.items():
            setattr(self, atributo, getattr(self, atributo) + valor)

    def atacar(self, alvo: Personagem) -> int:
        resultado = rolar_dado(20)

        if resultado >= 18:
            dano = rolar_dado(6) * 2
            critico = True
        else:
            dano = rolar_dado(6)
            critico = False

        modificador = (self.destreza - 10) // 2
        dano += modificador

        alvo.receber_dano(dano)

        if critico:
            print(f"🏹 {self.nome} dispara em {alvo.nome}: {dano} de dano CRÍTICO!")
        else:
            print(f"🏹 {self.nome} dispara em {alvo.nome}: {dano} de dano.")

        return dano