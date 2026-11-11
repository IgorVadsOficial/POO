class Elevador:
    def __init__(self):
        self.__andar_atual = 0
        self.__total_andares = 0
        self.__capacidade = 0
        self.__pessoas_presentes = 0

    def get_andar_atual(self):
        return self.__andar_atual

    def getTotal_andares(self):
        return self.__total_andares

    def getCapacidade(self):
        return self.__capacidade

    def get_pessoas_presentes(self):
        return self.__pessoas_presentes

    def __tem_gente(self) -> bool:
        if self.get_pessoas_presentes() > 0:
            return True
        else:
            return False

    def __tem_espaco(self) -> bool:
        if self.get_pessoas_presentes() < self.getCapacidade():
            return True
        else:
            return False

    def __pode_subir(self) -> bool:
        if self.get_andar_atual() < self.getTotal_andares():
            return True
        else:
            return False

    def __pode_descer(self) -> bool:
        if self.get_andar_atual() >= 1:
            return True
        else:
            return False

    def set_andar_atual(self, andar):
        if andar >= 0 and andar <= self.getTotal_andares():
            self.__andar_atual = andar
        else:
            print("Erro: andar inválido.")

    def set_capacidade(self, capacidade):
        if capacidade > 0:
            self.__capacidade = capacidade
        else:
            print("Erro: capacidade deve ser maior que zero.")

    def set_total_andares(self, andares):
        if andares >= 0:
            self.__total_andares = andares
        else:
            print("Erro: total de andares não pode ser negativo.")

    def set_pessoas_presentes(self, pessoas: int):
        if pessoas >= 0 and pessoas <= self.getCapacidade():
            self.__pessoas_presentes = pessoas
        else:
            print("Erro: quantidade de pessoas inválida.")

    def inicializar(self, capacidade: int, total_andares: int) -> None:
        self.set_capacidade(capacidade)
        self.set_total_andares(total_andares)

    def entrar(self) -> None:
        if self.__tem_espaco() == True:
            self.set_pessoas_presentes(self.get_pessoas_presentes() + 1)
            print(f"{self.get_pessoas_presentes()} pessoas")
        else:
            print("Erro: elevador lotado!")

    def sair(self):
        if self.__tem_gente() == True:
            self.set_pessoas_presentes(self.get_pessoas_presentes() - 1)
            print(f"{self.get_pessoas_presentes()} pessoas")
        else:
            print("Erro: elevador vazio!")

    def subir(self):
        if self.__pode_subir() == True:
            self.set_andar_atual(self.get_andar_atual() + 1)
        else:
            print("Erro você está no último andar!")

    def descer(self):
        if self.__pode_descer() == True:
            self.set_andar_atual(self.get_andar_atual() - 1)
        else:
            print("Erro: você está no térreo!")


elevador = Elevador()
elevador.inicializar(3, 5)

elevador.entrar()
elevador.entrar()
elevador.entrar()
elevador.entrar()

elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()
elevador.subir()

elevador.sair()
elevador.sair()
elevador.sair()
elevador.sair()

print("Andar:", elevador.get_andar_atual())
print("Pessoas:", elevador.get_pessoas_presentes())

elevador.set_capacidade(0)
elevador.set_total_andares(-1)
elevador.set_pessoas_presentes(10)
