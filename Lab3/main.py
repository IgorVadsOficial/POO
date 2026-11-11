"""Ponto de entrada do Lab 3 — Herança."""

from racas import Guerreiro, Mago

def main():
    guerreiro = Guerreiro("Arador")
    mago = Mago("Elara")
    guerreiro.exibir_ficha_rich()
    mago.exibir_ficha_rich()
    #
    # Confirme: Guerreiro.forca > Personagem().forca (bônus aplicado)
    print(guerreiro.forca, mago.inteligencia)


if __name__ == "__main__":
    main()
