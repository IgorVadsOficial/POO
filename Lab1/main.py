"""Ponto de entrada do Lab 1 — Forja de Heróis."""

from personagem import Personagem


def main():
    """Cria dois personagens e compara seus níveis."""
    heroi1 = Personagem(str(input("Digite o nome do 1° personagem: ")))
    heroi2 = Personagem(str(input("Digite o nome do 2° personagem: ")))

    heroi1.exibir_ficha()
    print()
    heroi2.exibir_ficha()
    print()

    if heroi1.nivel_total() > heroi2.nivel_total():
        print(f"{heroi1.nome} tem o maior nível total!")
    elif heroi2.nivel_total() > heroi1.nivel_total():
        print(f"{heroi2.nome} tem o maior nível total!")
    else:
        print(f"{heroi1.nome} e {heroi2.nome} empataram no nível total!")

if __name__ == "__main__":
    main()
