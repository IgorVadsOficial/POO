from __future__ import annotations


class Pessoa:
    def __init__(self, codigo: int, nome: str):
        self._codigo = codigo
        self._nome = nome

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return f"{self._nome}"


class Funcionario(Pessoa):
    def __init__(self, codigo: int, nome: str, cargo: str):
        super().__init__(codigo, nome)
        self._cargo = cargo

    @property
    def cargo(self):
        return self._cargo


class Operador(Funcionario):
    def __init__(self, codigo: int, nome: str, cargo: str = "Operador"):
        super().__init__(codigo, nome, cargo)

    def criar_reserva(
        self, voo: "Voo", passageiro: "Passageiro", empresa: "EmpresaAerea"
    ):
        return empresa.criar_reserva(voo, passageiro, self)

    def cancelar_reserva(self, reserva: "Reserva", empresa: "EmpresaAerea"):
        empresa.cancelar_reserva(reserva)


class Passageiro(Pessoa):
    def __init__(self, codigo: int, nome: str):
        super().__init__(codigo, nome)
        self._reservas = []

    @property
    def reservas(self):
        return self._reservas

    def criar_reserva(self, voo: "Voo", empresa: "EmpresaAerea"):
        return empresa.criar_reserva(voo, self, None)

    def cancelar_reserva(self, reserva: "Reserva", empresa: "EmpresaAerea"):
        empresa.cancelar_reserva(reserva)

    def pagar_reserva(self, reserva: "Reserva"):
        reserva.pagar()


class Aeroporto:
    def __init__(self, nome: str, cidade: str, capacidade_decolagens_por_hora: int):
        self._nome = nome
        self._cidade = cidade
        self._capacidade_decolagens_por_hora = capacidade_decolagens_por_hora

    @property
    def nome(self):
        return self._nome

    @property
    def cidade(self):
        return self._cidade

    @property
    def capacidade_decolagens_por_hora(self):
        return self._capacidade_decolagens_por_hora

    def __str__(self):
        return f"{self._nome} ({self._cidade})"


class Reserva:
    def __init__(
        self,
        codigo: int,
        voo: "Voo",
        passageiro: Passageiro,
        operador: Operador | None = None,
    ):
        self._codigo = codigo
        self._voo = voo
        self._passageiro = passageiro
        self._operador = operador
        self._status = "ativa"

    @property
    def codigo(self):
        return self._codigo

    @property
    def voo(self):
        return self._voo

    @property
    def passageiro(self):
        return self._passageiro

    @property
    def operador(self):
        return self._operador

    @property
    def status(self):
        return self._status

    def pagar(self):
        if self._status == "cancelada":
            raise ValueError("Não é possível pagar uma reserva cancelada.")
        self._status = "paga"
        return True

    def cancelar(self):
        if self._status == "cancelada":
            return False
        self._status = "cancelada"
        self._voo.remover_reserva(self)
        return True

    def __str__(self):
        return f"Reserva #{self._codigo} - {self._passageiro.nome} - {self._voo.codigo} - {self._status}"


class Voo:
    def __init__(
        self,
        codigo: str,
        horario: str,
        data: str,
        aeroporto_origem: Aeroporto,
        aeroporto_destino: Aeroporto,
        tipo: str,
        total_assentos: int,
    ):
        self._codigo = codigo
        self._horario = horario
        self._data = data
        self._aeroporto_origem = aeroporto_origem
        self._aeroporto_destino = aeroporto_destino
        self._tipo = tipo
        self._total_assentos = total_assentos
        self._assentos_livres = total_assentos
        self._tripulacao = []
        self._reservas = []

    @property
    def codigo(self):
        return self._codigo

    @property
    def horario(self):
        return self._horario

    @property
    def data(self):
        return self._data

    @property
    def aeroporto_origem(self):
        return self._aeroporto_origem

    @property
    def aeroporto_destino(self):
        return self._aeroporto_destino

    @property
    def tipo(self):
        return self._tipo

    @property
    def tripulacao(self):
        return self._tripulacao

    @property
    def assentos_livres(self):
        return self._assentos_livres

    @property
    def reservas(self):
        return self._reservas

    def adicionar_tripulante(self, funcionario: Funcionario):
        if funcionario not in self._tripulacao:
            self._tripulacao.append(funcionario)

    def remover_tripulante(self, funcionario: Funcionario):
        if funcionario in self._tripulacao:
            self._tripulacao.remove(funcionario)

    def adicionar_reserva(self, reserva: Reserva):
        if self._assentos_livres <= 0:
            raise ValueError("Não há assentos disponíveis para este voo.")
        self._reservas.append(reserva)
        self._assentos_livres -= 1

    def remover_reserva(self, reserva: Reserva):
        if reserva in self._reservas:
            self._reservas.remove(reserva)
            self._assentos_livres += 1

    def __str__(self):
        return (
            f"Voo {self._codigo} - {self._data} às {self._horario} - "
            f"{self._aeroporto_origem} -> {self._aeroporto_destino} "
            f"({self._tipo}) - Assentos livres: {self._assentos_livres}"
        )


class EmpresaAerea:
    def __init__(self):
        self._aeroportos = []
        self._voos = []
        self._passageiros = []
        self._operadores = []
        self._reservas = []

    @property
    def aeroportos(self):
        return self._aeroportos

    @property
    def voos(self):
        return self._voos

    @property
    def passageiros(self):
        return self._passageiros

    @property
    def operadores(self):
        return self._operadores

    @property
    def reservas(self):
        return self._reservas

    def cadastrar_aeroporto(self, nome: str, cidade: str, capacidade: int):
        aeroporto = Aeroporto(nome, cidade, capacidade)
        self._aeroportos.append(aeroporto)
        return aeroporto

    def cadastrar_voo(
        self,
        codigo: str,
        horario: str,
        data: str,
        origem: Aeroporto,
        destino: Aeroporto,
        tipo: str,
        total_assentos: int,
    ):
        voo = Voo(codigo, horario, data, origem, destino, tipo, total_assentos)
        self._voos.append(voo)
        return voo

    def cadastrar_passageiro(self, codigo: int, nome: str):
        passageiro = Passageiro(codigo, nome)
        self._passageiros.append(passageiro)
        return passageiro

    def cadastrar_operador(self, codigo: int, nome: str, cargo: str = "Operador"):
        operador = Operador(codigo, nome, cargo)
        self._operadores.append(operador)
        return operador

    def criar_reserva(
        self, voo: Voo, passageiro: Passageiro, operador: Operador | None = None
    ):
        if voo is None or passageiro is None:
            raise ValueError("Voo e passageiro são obrigatórios.")
        if voo.assentos_livres <= 0:
            raise ValueError("Voo sem assentos disponíveis.")

        reserva = Reserva(len(self._reservas) + 1, voo, passageiro, operador)
        voo.adicionar_reserva(reserva)
        passageiro.reservas.append(reserva)
        self._reservas.append(reserva)
        return reserva

    def cancelar_reserva(self, reserva: Reserva):
        if reserva in self._reservas:
            reserva.cancelar()
            self._reservas.remove(reserva)
            return True
        raise ValueError("Reserva não encontrada.")

    def listar_voos(self):
        for voo in self._voos:
            print(voo)

    def listar_reservas(self):
        for reserva in self._reservas:
            print(reserva)


def mostrar_menu():
    print("\n=== Sistema de Empresa Aérea ===")
    print("1 - Cadastrar aeroporto")
    print("2 - Cadastrar voo")
    print("3 - Cadastrar passageiro")
    print("4 - Cadastrar operador")
    print("5 - Criar reserva")
    print("6 - Pagar reserva")
    print("7 - Cancelar reserva")
    print("8 - Listar voos")
    print("9 - Listar reservas")
    print("0 - Sair")


def executar_menu():
    empresa = EmpresaAerea()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Sistema encerrado.")
            break

        elif opcao == "1":
            nome = input("Nome do aeroporto: ")
            cidade = input("Cidade: ")
            capacidade = int(input("Capacidade de decolagens por hora: "))
            empresa.cadastrar_aeroporto(nome, cidade, capacidade)
            print("Aeroporto cadastrado com sucesso.")

        elif opcao == "2":
            codigo = input("Código do voo: ")
            horario = input("Horário do voo: ")
            data = input("Data do voo: ")
            origem = input("Aeroporto de origem: ")
            destino = input("Aeroporto de destino: ")
            tipo = input("Tipo do voo (nacional/internacional): ")
            assentos = int(input("Quantidade de assentos: "))

            aeroporto_origem = next(
                (a for a in empresa.aeroportos if a.nome.lower() == origem.lower()),
                None,
            )
            aeroporto_destino = next(
                (a for a in empresa.aeroportos if a.nome.lower() == destino.lower()),
                None,
            )

            if aeroporto_origem is None or aeroporto_destino is None:
                print("Aeroportos informados não foram encontrados.")
                continue

            empresa.cadastrar_voo(
                codigo,
                horario,
                data,
                aeroporto_origem,
                aeroporto_destino,
                tipo,
                assentos,
            )
            print("Voo cadastrado com sucesso.")

        elif opcao == "3":
            codigo = int(input("Código do passageiro: "))
            nome = input("Nome do passageiro: ")
            empresa.cadastrar_passageiro(codigo, nome)
            print("Passageiro cadastrado com sucesso.")

        elif opcao == "4":
            codigo = int(input("Código do operador: "))
            nome = input("Nome do operador: ")
            cargo = input("Cargo: ")
            empresa.cadastrar_operador(codigo, nome, cargo)
            print("Operador cadastrado com sucesso.")

        elif opcao == "5":
            codigo_voo = input("Código do voo: ")
            voo = next(
                (v for v in empresa.voos if v.codigo.lower() == codigo_voo.lower()),
                None,
            )
            if voo is None:
                print("Voo não encontrado.")
                continue

            codigo_passageiro = int(input("Código do passageiro: "))
            passageiro = next(
                (p for p in empresa.passageiros if p.codigo == codigo_passageiro), None
            )
            if passageiro is None:
                print("Passageiro não encontrado.")
                continue

            operador = None
            if empresa.operadores:
                print("Operadores disponíveis:")
                for op in empresa.operadores:
                    print(f"{op.codigo} - {op.nome}")
                codigo_operador = input(
                    "Código do operador (opcional, deixe em branco para ignorar): "
                )
                if codigo_operador.strip():
                    operador = next(
                        (
                            op
                            for op in empresa.operadores
                            if op.codigo == int(codigo_operador)
                        ),
                        None,
                    )

            reserva = empresa.criar_reserva(voo, passageiro, operador)
            print(f"Reserva criada: {reserva}")

        elif opcao == "6":
            codigo = int(input("Código da reserva: "))
            reserva = next((r for r in empresa.reservas if r.codigo == codigo), None)
            if reserva is None:
                print("Reserva não encontrada.")
                continue
            reserva.pagar()
            print(f"Reserva paga: {reserva}")

        elif opcao == "7":
            codigo = int(input("Código da reserva: "))
            reserva = next((r for r in empresa.reservas if r.codigo == codigo), None)
            if reserva is None:
                print("Reserva não encontrada.")
                continue
            empresa.cancelar_reserva(reserva)
            print(f"Reserva cancelada: {reserva}")

        elif opcao == "8":
            if not empresa.voos:
                print("Nenhum voo cadastrado.")
            else:
                empresa.listar_voos()

        elif opcao == "9":
            if not empresa.reservas:
                print("Nenhuma reserva cadastrada.")
            else:
                empresa.listar_reservas()

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar_menu()
