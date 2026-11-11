class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


p1 = Pessoa(
    input("Nome: ").strip().capitalize(),
    int(input("Idade: ")),
    float(input("Peso [KG]: ")),
    float(input("Altura [cm]: ")),
)


def envelhecer(self):
    while self.idade < 21:
        self.idade += 1
        self.altura += 0.5
        print(
            f"{self.nome} completou {self.idade} anos idade e agora tem {self.altura}cm de altura."
        )


def engordar(self):
    quer = str(input("Gostaria de adicionar peso? [S/N] ")).strip().upper()[0]

    while quer not in ("S", "N"):
        quer = (
            str(input("Resposta inválida! Gostaria de adicionar peso? Sim ou Não? "))
            .strip()
            .upper()[0]
        )

    if quer == "S":
        peso_adicional = float(input("Adicionar quantos KG: "))
        self.peso += peso_adicional
        print(f"{self.nome} agora tem: {self.peso}KG")
    else:
        print("")


def emagrecer(self):
    quer = str(input("Gostaria de remover peso? [S/N] ")).strip().upper()[0]

    while quer not in ("S", "N"):
        quer = (
            str(input("Resposta inválida! Gostaria de remover peso? Sim ou Não? "))
            .strip()
            .upper()[0]
        )

    if quer == "S":
        peso_removido = float(input("Remover quantos KG:  "))
        if peso_removido <= self.peso:
            self.peso -= peso_removido
        else:
            while peso_removido > self.peso:
                print("Você não pode revolver mais peso do que tem! ")
                peso_removido = float(input("Gostaria de remover quantos KG:  "))
            self.peso -= peso_removido
        print(f"{self.nome} agora tem: {self.peso}KG")
    else:
        print("")


def crescer(self):
    quer = str(input("Gostaria de adicionar altura? [S/N] ")).strip().upper()[0]

    while quer not in ("S", "N"):
        quer = (
            str(input("Resposta inválida! Gostaria de adicionar altura? Sim ou Não? "))
            .strip()
            .upper()[0]
        )

    if quer == "S":
        altura_adicional = float(input("Altura: "))
        self.peso += altura_adicional
        print(f"{self.nome} agora tem: {self.altura}m")
    else:
        print("")


envelhecer(p1)
print("-" * 30)
engordar(p1)
print("-" * 30)
emagrecer(p1)
print("-" * 30)
crescer(p1)
