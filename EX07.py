from calendar import isleap


class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes

    def get_ano(self):
        return self.__ano

    def set_mes(self, mes: int):
        if mes > 0 and mes <= 12:
            self.__mes = mes
        else:
            while mes < 0 and mes > 12:
                mes = int(input("Mês inválido, Digita entre 1 e 12: "))
            self.__mes = mes

    def set_ano(self, ano: int):
        self.__ano = ano

    def ano_bisexto(self):
        isleap(self.get_ano())

    def set_dia(self, dia: int):
        if self.get_mes() == 1 and (dia > 0 and dia < 32):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 32:
                dia = int(input("Dia inválido, digite entre 1 e 31: "))
            self.__dia = dia

        if (
            self.get_mes() == 2
            and self.ano_bisexto() == False
            and (dia > 0 and dia < 29)
        ):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 29:
                dia = int(input("Dia inválido, digite entre 1 e 28: "))
            self.__dia = dia

        if (
            self.get_mes() == 2
            and self.ano_bisexto() == True
            and (dia > 0 and dia <= 29)
        ):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 30:
                dia = int(input("Dia inválido, digite entre 1 e 29: "))
            self.__dia = dia

        if self.get_mes() == 3 and (dia > 0 and dia < 32):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 32:
                dia = int(input("Dia inválido, digite entre 1 e 31: "))
            self.__dia = dia

        if self.get_mes() == 4 and (dia > 0 and dia < 31):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 31:
                dia = int(input("Dia inválido, digite entre 1 e 30: "))
            self.__dia = dia

        if self.get_mes() == 5 and (dia > 0 and dia < 32):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 32:
                dia = int(input("Dia inválido, digite entre 1 e 31: "))
            self.__dia = dia

        if self.get_mes() == 6 and (dia > 0 and dia < 31):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 31:
                dia = int(input("Dia inválido, digite entre 1 e 30: "))
            self.__dia = dia

        if self.get_mes() == 7 and (dia > 0 and dia < 32):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 32:
                dia = int(input("Dia inválido, digite entre 1 e 31: "))
            self.__dia = dia

        if self.get_mes() == 8 and (dia > 0 and dia < 32):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 32:
                dia = int(input("Dia inválido, digite entre 1 e 31: "))
            self.__dia = dia

        if self.get_mes() == 9 and (dia > 0 and dia < 31):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 31:
                dia = int(input("Dia inválido, digite entre 1 e 30: "))
            self.__dia = dia

        if self.get_mes() == 10 and (dia > 0 and dia < 32):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 32:
                dia = int(input("Dia inválido, digite entre 1 e 31: "))
            self.__dia = dia

        if self.get_mes() == 11 and (dia > 0 and dia < 31):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 31:
                dia = int(input("Dia inválido, digite entre 1 e 30: "))
            self.__dia = dia

        if self.get_mes() == 12 and (dia > 0 and dia < 32):
            self.__dia = dia
        else:
            while dia <= 0 and dia >= 32:
                dia = int(input("Dia inválido, digite entre 1 e 31: "))
            self.__dia = dia

    def exibir_data(self):
        print(f"{self.get_dia()}/{self.get_mes()}/{self.get_ano()}")


data1 = Data(0, 0, 0)

data1.set_dia(16)
data1.set_mes(9)
data1.set_ano(2026)

data1.exibir_data()
