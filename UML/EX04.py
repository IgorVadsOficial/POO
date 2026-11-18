class Aeroporto:
    def __init__(self, nome, cidade, pais, capacidade):
        self.nome = nome
        self.cidade = cidade
        self.pais = pais
        self.capacidade = capacidade  # decolagens por hora


class Aeroviario:
    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao


class Voo:
    def __init__(self, codigo, horario, data, partida, destino, assentos):
        self.codigo = codigo
        self.horario = horario
        self.data = data
        self.partida = partida
        self.destino = destino
        self.assentos = assentos      # total de assentos do avião
        self.reservas = []
        self.tripulacao = []

    def assentos_livres(self):
        return self.assentos - len(self.reservas)

    def get_tripulacao(self):
        return self.tripulacao

    def get_tipo(self):
        if self.partida.pais == self.destino.pais:
            return "NACIONAL"
        return "INTERNACIONAL"


class Reserva:
    contador = 0

    def __init__(self, passageiro, voo):
        Reserva.contador += 1
        self.codigo = "R" + str(Reserva.contador)
        self.passageiro = passageiro
        self.voo = voo
        self.paga = False


class Passageiro:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.reservas = []

    def criar_reserva(self, voo):
        if voo.assentos_livres() == 0:
            return None
        reserva = Reserva(self, voo)
        voo.reservas.append(reserva)
        self.reservas.append(reserva)
        return reserva

    def cancelar_reserva(self, reserva):
        reserva.voo.reservas.remove(reserva)
        self.reservas.remove(reserva)

    def pagar_reserva(self, reserva):
        reserva.paga = True


class Operador:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def criar_reserva(self, passageiro, voo):
        return passageiro.criar_reserva(voo)

    def cancelar_reserva(self, reserva):
        reserva.passageiro.cancelar_reserva(reserva)


# ---------------- dados de exemplo ----------------
natal = Aeroporto("Aeroporto de Natal", "Natal", "Brasil", 20)
saopaulo = Aeroporto("Guarulhos", "São Paulo", "Brasil", 60)
lisboa = Aeroporto("Humberto Delgado", "Lisboa", "Portugal", 40)

voos = [
    Voo("AD100", "08:00", "20/12/2026", natal, saopaulo, 3),
    Voo("AD200", "14:30", "21/12/2026", saopaulo, lisboa, 2),
    Voo("AD300", "22:15", "22/12/2026", lisboa, natal, 2),
]
for v in voos:
    v.tripulacao.append(Aeroviario("Carlos", "Piloto"))
    v.tripulacao.append(Aeroviario("Marina", "Comissária"))

operador = Operador("Ana", "OP01")
passageiros = {}  # cpf -> Passageiro


# ---------------- interface ----------------
def listar_voos():
    print("\nVoos disponíveis:")
    for i, v in enumerate(voos, 1):
        print(f"{i}) {v.codigo} | {v.partida.cidade} -> {v.destino.cidade} | "
              f"{v.data} {v.horario} | {v.get_tipo()} | "
              f"assentos livres: {v.assentos_livres()}")


def escolher_voo():
    listar_voos()
    try:
        return voos[int(input("Número do voo: ")) - 1]
    except (ValueError, IndexError):
        print("Voo inválido.")
        return None


def escolher_reserva(passageiro):
    if not passageiro.reservas:
        print("Esse passageiro não tem reservas.")
        return None
    for r in passageiro.reservas:
        print(f"{r.codigo} | voo {r.voo.codigo} | paga: {'sim' if r.paga else 'não'}")
    codigo = input("Código da reserva: ").strip().upper()
    for r in passageiro.reservas:
        if r.codigo == codigo:
            return r
    print("Reserva não encontrada.")
    return None


def identificar_passageiro():
    cpf = input("CPF do passageiro: ").strip()
    if cpf not in passageiros:
        passageiros[cpf] = Passageiro(input("Nome: ").strip(), cpf)
    return passageiros[cpf]


def menu_passageiro():
    p = identificar_passageiro()
    print("Olá,", p.nome)
    while True:
        print("\n--- PASSAGEIRO ---")
        print("1) Listar voos  2) Criar reserva  3) Cancelar reserva")
        print("4) Pagar reserva  5) Ver tripulação  0) Voltar")
        op = input("Opção: ").strip()
        if op == "1":
            listar_voos()
        elif op == "2":
            voo = escolher_voo()
            if voo:
                r = p.criar_reserva(voo)
                print("Reserva criada:", r.codigo) if r else print("Voo lotado.")
        elif op == "3":
            r = escolher_reserva(p)
            if r:
                p.cancelar_reserva(r)
                print("Reserva cancelada.")
        elif op == "4":
            r = escolher_reserva(p)
            if r:
                p.pagar_reserva(r)
                print("Reserva paga.")
        elif op == "5":
            voo = escolher_voo()
            if voo:
                for a in voo.get_tripulacao():
                    print("-", a.nome, "(" + a.funcao + ")")
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def menu_operador():
    print("Olá, operador", operador.nome)
    while True:
        print("\n--- OPERADOR ---")
        print("1) Listar voos  2) Criar reserva  3) Cancelar reserva  0) Voltar")
        op = input("Opção: ").strip()
        if op == "1":
            listar_voos()
        elif op == "2":
            p = identificar_passageiro()
            voo = escolher_voo()
            if voo:
                r = operador.criar_reserva(p, voo)
                print("Reserva criada:", r.codigo) if r else print("Voo lotado.")
        elif op == "3":
            p = identificar_passageiro()
            r = escolher_reserva(p)
            if r:
                operador.cancelar_reserva(r)
                print("Reserva cancelada.")
        elif op == "0":
            break
        else:
            print("Opção inválida.")


def main():
    while True:
        print("\n=== EMPRESA AÉREA ===")
        print("1) Sou passageiro  2) Sou operador  0) Sair")
        op = input("Opção: ").strip()
        if op == "1":
            menu_passageiro()
        elif op == "2":
            menu_operador()
        elif op == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


main()
