from abc import ABC, abstractmethod


class Atacante(ABC):
    @abstractmethod
    def chutar_ao_gol(self):
        pass


class Defensor(ABC):
    @abstractmethod
    def bloquear_chute(self):
        pass


class Meiocampista(ABC):
    @abstractmethod
    def dar_assistencia(self):
        pass


class Goleiro(ABC):
    @abstractmethod
    def defender_penalti(self):
        pass


class Jogador1(Atacante, Meiocampista):
    def chutar_ao_gol(self):
        print("Jogador1 chutou no gol")

    def dar_assistencia(self):
        print("Jogador1 deu uma assistencia")


class Jogador2(Defensor, Goleiro, Meiocampista):
    def bloquear_chute(self):
        print("Jogador2 bloqueou o chute do atacante")

    def dar_assistencia(self):
        print("Jogador2 deu uma assistencia")

    def defender_penalti(self):
        print("Jogador 2 defendeu o chute a gol")


j1 = Jogador1()
j1.chutar_ao_gol()
j1.dar_assistencia()

j2 = Jogador2()
j2.bloquear_chute()
j2.dar_assistencia()
