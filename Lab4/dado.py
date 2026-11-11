"""
Módulo de utilitários para rolagem de dados.

Este módulo é importado por outros módulos do projeto Forja de Heróis.
"""

import random


def rolar_dado(lados: int = 6) -> int:
    """Rola um dado com o número de lados especificado.

    Args:
        lados: Número de lados do dado. Padrão: 6.

    Returns:
        Resultado inteiro entre 1 e lados (inclusive).
    """
    return random.randint(1, lados)


def rolar_atributo() -> int:
    """Rola 4d6 e descarta o menor resultado (método padrão D&D 5e).

    Returns:
        Soma dos 3 maiores resultados de 4 rolagens de d6.
    """
    rolagens = [rolar_dado(6) for _ in range(4)]
    rolagens.remove(min(rolagens))
    return sum(rolagens)


def rolar_todos_atributos() -> dict:
    """Rola os 6 atributos de um personagem.

    Returns:
        Dicionário com chaves FOR, DES, CON, SAB, INT, CAR.
    """
    return {
        "FOR": rolar_atributo(),
        "DES": rolar_atributo(),
        "CON": rolar_atributo(),
        "SAB": rolar_atributo(),
        "INT": rolar_atributo(),
        "CAR": rolar_atributo(),
    }
