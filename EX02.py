class Conta:
    def __init__(self, numero, titular, saldo, limite, codigo_tipo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_tipo = codigo_tipo

        if codigo_tipo == 1:
            self.nome_tipo = "conta corrente"
        elif codigo_tipo == 2:
            self.nome_tipo = "poupança"
        else:
            self.nome_tipo = "desconhecido"

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def extrato(self):
        print(f"Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Tipo: {self.nome_tipo} (código {self.codigo_tipo})")
        print(f"Saldo: R${self.saldo:.2f}")
        print(f"Limite: R${self.limite:.2f}")
        print("-" * 30)


def transferir(self, destino, valor):
    if self.saca(valor):
        destino.deposita(valor)
        print(f"\nTransferência de R${valor:.2f} realizada com sucesso!")
        print(f"De: {self.titular} (Conta {self.numero})")
        print(f"Para: {destino.titular} (Conta {destino.numero})")
        return True
    else:
        print("Transferência não realizada!")
        return False


print("== DADOS DA PRIMEIRA CONTA===")
c1 = Conta(
    int(input("Numero: ")),
    input("Titular: ").strip().capitalize(),
    float(input("Saldo: ")),
    float(input("Limite: ")),
    int(input("Tipo: ")),
)

print("\n== DADOS DA SEGUNDA CONTA ==")
c2 = Conta(
    int(input("Numero: ")),
    input("Titular: ").strip().capitalize(),
    float(input("Saldo: ")),
    float(input("Limite: ")),
    int(input("Tipo: ")),
)

valor = float(input("Quanto deseja transferir? R$"))

transferir(c1, c2, valor)
print("-" * 30)
print("\n")
c1.extrato()
print("\n")
c2.extrato()
