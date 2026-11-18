# Exercício 4 - Empresa Aérea com interface de interação com o usuário
# Programa de console: o usuário escolhe opções num menu digitando números.


# ======================================================================
# CLASSES (seguem o diagrama UML)
# ======================================================================

class Aeroporto:
    """Representa um aeroporto (usado como partida ou destino de um voo)."""

    def __init__(self, nome, cidade, pais, capacidade):
        self.nome = nome
        self.cidade = cidade
        self.pais = pais
        self.capacidade = capacidade  # decolagens por hora


class Aeroviario:
    """Funcionário que faz parte da tripulação de um voo."""

    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao  # ex.: Piloto, Comissário


class Reserva:
    """Reserva de um passageiro em um voo."""

    contador = 0  # atributo da classe: conta quantas reservas já foram criadas

    def __init__(self, voo, passageiro):
        Reserva.contador += 1
        self.codigo = f"R{Reserva.contador}"  # gera R1, R2, R3...
        self.paga = False                     # toda reserva começa como não paga
        self.voo = voo                        # cada reserva pertence a um voo
        self.passageiro = passageiro          # e possui um passageiro


class Voo:
    """Voo com horário, data, aeroportos, tripulação e lista de reservas."""

    def __init__(self, codigo, horario, data, partida, destino, assentos, tripulacao):
        self.codigo = codigo
        self.horario = horario
        self.data = data
        self.partida = partida        # objeto Aeroporto
        self.destino = destino        # objeto Aeroporto
        self.assentos = assentos      # total de assentos do voo
        self.tripulacao = tripulacao  # lista de Aeroviario
        self.reservas = []            # um voo tem várias reservas (0..*)

    def assentos_livres(self):
        # assentos totais menos os já reservados
        return self.assentos - len(self.reservas)

    def get_tripulacao(self):
        return self.tripulacao

    def get_tipo(self):
        # se os dois aeroportos estão no mesmo país, o voo é nacional
        return "Nacional" if self.partida.pais == self.destino.pais else "Internacional"


class Passageiro:
    """Pessoa que compra voos: pode criar, cancelar e pagar reservas."""

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def criar_reserva(self, voo):
        if voo.assentos_livres() == 0:
            return None                      # voo lotado, não cria a reserva
        reserva = Reserva(voo, self)
        voo.reservas.append(reserva)         # registra a reserva dentro do voo
        return reserva

    def cancelar_reserva(self, reserva):
        reserva.voo.reservas.remove(reserva)  # tira a reserva do voo

    def pagar_reserva(self, reserva):
        reserva.paga = True


class Operador:
    """Funcionário que cria e cancela reservas em nome dos passageiros."""

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def criar_reserva(self, voo, passageiro):
        # reaproveita a lógica do passageiro
        return passageiro.criar_reserva(voo)

    def cancelar_reserva(self, reserva):
        reserva.passageiro.cancelar_reserva(reserva)


# ======================================================================
# DADOS DE EXEMPLO (já deixam o sistema pronto para testar)
# ======================================================================

natal = Aeroporto("Augusto Severo", "Natal", "Brasil", 20)
sao_paulo = Aeroporto("Guarulhos", "Sao Paulo", "Brasil", 60)
lisboa = Aeroporto("Humberto Delgado", "Lisboa", "Portugal", 40)

equipe = [Aeroviario("Ana", "Piloto"), Aeroviario("Bruno", "Comissario")]

# Voo(codigo, horario, data, partida, destino, assentos, tripulacao)
voos = [
    Voo("V100", "08:00", "20/11/2026", natal, sao_paulo, 3, equipe),
    Voo("V200", "22:30", "25/11/2026", sao_paulo, lisboa, 2, equipe),
]

passageiros = {}  # dicionário {cpf: Passageiro} com quem já usou o sistema


# ======================================================================
# FUNÇÕES AUXILIARES DA INTERFACE
# ======================================================================

def obter_passageiro(cpf):
    # se o CPF ainda não existe, pede o nome e cadastra o passageiro
    if cpf not in passageiros:
        passageiros[cpf] = Passageiro(input("Nome: "), cpf)
    return passageiros[cpf]


def escolher_voo():
    # pede o código e procura o voo; devolve None se não achar
    codigo = input("Codigo do voo: ").upper()
    return next((v for v in voos if v.codigo == codigo), None)


def achar_reserva(codigo):
    # procura a reserva em todos os voos; devolve None se não achar
    for v in voos:
        for r in v.reservas:
            if r.codigo == codigo.upper():
                return r
    return None


def listar_voos():
    for v in voos:
        print(f"{v.codigo} | {v.get_tipo()} | {v.partida.cidade} -> {v.destino.cidade} | "
              f"{v.data} {v.horario} | livres: {v.assentos_livres()} | "
              f"tripulacao: {', '.join(a.nome for a in v.get_tripulacao())}")


def listar_reservas():
    for v in voos:
        for r in v.reservas:
            print(f"{r.codigo} | {v.codigo} | {r.passageiro.nome} | {'paga' if r.paga else 'nao paga'}")


# ======================================================================
# MENU PRINCIPAL DE CADA TIPO DE USUÁRIO
# ======================================================================

def menu(usuario, e_operador):
    # o mesmo menu serve para passageiro e operador; só mudam algumas opções
    while True:
        print("\n1-Listar voos  2-Criar reserva  3-Cancelar reserva", end="")
        print("  4-Listar reservas  0-Sair" if e_operador else "  4-Pagar reserva  5-Minhas reservas  0-Sair")
        op = input("> ")

        if op == "0":                         # sair do menu
            break

        elif op == "1":                       # listar voos
            listar_voos()

        elif op == "2":                       # criar reserva
            voo = escolher_voo()
            if not voo:
                print("Voo nao encontrado.")
                continue
            if e_operador:
                # operador cria a reserva para um passageiro (identificado pelo CPF)
                reserva = usuario.criar_reserva(voo, obter_passageiro(input("CPF do passageiro: ")))
            else:
                # passageiro cria a reserva para si mesmo
                reserva = usuario.criar_reserva(voo)
            print(f"Reserva {reserva.codigo} criada." if reserva else "Voo lotado.")

        elif op in ("3", "4") and not (op == "4" and e_operador):
            # opção 3 (cancelar) para todos; opção 4 (pagar) só para passageiro
            reserva = achar_reserva(input("Codigo da reserva: "))
            # passageiro só mexe nas próprias reservas; operador mexe em qualquer uma
            if not reserva or (not e_operador and reserva.passageiro is not usuario):
                print("Reserva nao encontrada.")
            elif op == "3":
                usuario.cancelar_reserva(reserva)
                print("Reserva cancelada.")
            else:
                usuario.pagar_reserva(reserva)
                print("Reserva paga.")

        elif op == "4":                       # (operador) listar todas as reservas
            listar_reservas()

        elif op == "5" and not e_operador:    # (passageiro) listar só as suas reservas
            for v in voos:
                for r in v.reservas:
                    if r.passageiro is usuario:
                        print(f"{r.codigo} | {v.codigo} | {'paga' if r.paga else 'nao paga'}")

        else:
            print("Opcao invalida.")


# ======================================================================
# PROGRAMA PRINCIPAL: escolhe o tipo de usuário e abre o menu
# ======================================================================

while True:
    tipo = input("\nEntrar como 1-Passageiro  2-Operador  0-Sair: ")
    if tipo == "0":
        break
    elif tipo == "1":
        menu(obter_passageiro(input("Seu CPF: ")), False)
    elif tipo == "2":
        menu(Operador(input("Nome: "), input("Matricula: ")), True)
