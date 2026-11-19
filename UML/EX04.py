from abc import ABC, abstractmethod


class Aeroporto:
    def __init__(self, nome, cidade, pais, capacidade):
        self.__nome = nome
        self.__cidade = cidade
        self.__pais = pais
        self.__capacidade = capacidade

    def getPais(self):
        return self.__pais


class Funcionario(ABC):
    def __init__(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    @abstractmethod
    def getCargo(self):
        pass


class Aeroviario(Funcionario):
    def __init__(self, nome, funcao):
        super().__init__(nome)
        self.__funcao = funcao

    def getFuncao(self):
        return self.__funcao

    def getCargo(self):
        return self.__funcao


class Voo:
    def __init__(self, codigo, horario, data, partida, destino, assentos):
        self.__codigo = codigo
        self.__horario = horario
        self.__data = data
        self.__partida = partida
        self.__destino = destino
        self.__assentos = assentos
        self.__reservas = []
        self.__tripulantes = []

    def assentosLivres(self):
        return self.__assentos - len(self.__reservas)

    def getTripulacao(self):
        return self.__tripulantes

    def getTipo(self):
        if self.__partida.getPais() == self.__destino.getPais():
            return "NACIONAL"
        return "INTERNACIONAL"

    def getReservas(self):
        return self.__reservas


class Reserva:
    def __init__(self, codigo, passageiro, voo, operador):
        self.__codigo = codigo
        self.__paga = False
        self.__passageiro = passageiro
        self.__voo = voo
        self.__operador = operador

    def getCodigo(self):
        return self.__codigo

    def getPaga(self):
        return self.__paga

    def setPaga(self, paga):
        self.__paga = paga

    def getVoo(self):
        return self.__voo


class Passageiro:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__reservas = []

    def criarReserva(self, voo, operador=None):
        if voo.assentosLivres() == 0:
            return None
        reserva = Reserva("R" + str(len(self.__reservas) + 1), self, voo, operador)
        voo.getReservas().append(reserva)
        self.__reservas.append(reserva)
        return reserva

    def cancelarReserva(self, reserva):
        reserva.getVoo().getReservas().remove(reserva)
        self.__reservas.remove(reserva)

    def pagarReserva(self, reserva):
        reserva.setPaga(True)

    def getReservas(self):
        return self.__reservas


class Operador(Funcionario):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.__matricula = matricula
        self.__reservas = []

    def criarReserva(self, passageiro, voo):
        reserva = passageiro.criarReserva(voo, self)
        if reserva:
            self.__reservas.append(reserva)
        return reserva

    def cancelarReserva(self, passageiro, reserva):
        passageiro.cancelarReserva(reserva)
        if reserva in self.__reservas:
            self.__reservas.remove(reserva)

    def getCargo(self):
        return "Operador"


natal = Aeroporto("Aeroporto de Natal", "Natal", "Brasil", 20)
lisboa = Aeroporto("Humberto Delgado", "Lisboa", "Portugal", 40)

voo = Voo("AD100", "08:00", "20/12/2026", natal, lisboa, 2)
voo.getTripulacao().append(Aeroviario("Carlos", "Piloto"))

passageiro = Passageiro(input("Nome do passageiro: "), "000")
operador = Operador("Ana", "OP01")
perfil = input("1 = passageiro, 2 = operador: ")


def escolher_reserva():
    for i, r in enumerate(passageiro.getReservas(), 1):
        print(i, "-", r.getCodigo(), "| paga:", r.getPaga())
    return passageiro.getReservas()[int(input("Qual reserva? ")) - 1]


while True:
    print("\nVoo", voo.getTipo(), "| assentos livres:", voo.assentosLivres())
    print("1 Reservar | 2 Cancelar | 3 Pagar | 4 Tripulação | 0 Sair")
    opcao = input("> ")

    if opcao == "1":
        if perfil == "1":
            reserva = passageiro.criarReserva(voo)
        else:
            reserva = operador.criarReserva(passageiro, voo)
        print("Reservado!" if reserva else "Voo cheio.")

    elif opcao == "2":
        reserva = escolher_reserva()
        if perfil == "1":
            passageiro.cancelarReserva(reserva)
        else:
            operador.cancelarReserva(passageiro, reserva)
        print("Cancelada.")

    elif opcao == "3":
        if perfil == "1":
            passageiro.pagarReserva(escolher_reserva())
            print("Paga!")
        else:
            print("Só o passageiro paga.")

    elif opcao == "4":
        for a in voo.getTripulacao():
            print("-", a.getNome(), a.getCargo())

    elif opcao == "0":
        break
