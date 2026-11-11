class CartaoMensagem:
    def __init__(self, nome_destinatario):
        self.nome_destinatario = nome_destinatario

    def mensagem(self):
        pass


class MensagemDiaDosNamorados(CartaoMensagem):
    def __init__(self, nome_destinatario):
        super().__init__(nome_destinatario)

    def mensagem(self):
        print(f"Feliz dia dos namorados, {self.nome_destinatario}, eu te amo!")


class MensagemNatal(CartaoMensagem):
    def __init__(self, nome_destinatario):
        super().__init__(nome_destinatario)

    def mensagem(self):
        print(f"Feliz Natal, {self.nome_destinatario}, boas festas!")


class MensagemAniversario(CartaoMensagem):
    def __init__(self, nome_destinatario):
        super().__init__(nome_destinatario)

    def mensagem(self):
        print(
            f"Feliz Aniversário, {self.nome_destinatario} lhe desejo muitos anos de vida."
        )


listaMsg = []

listaMsg.append(MensagemDiaDosNamorados("Eduarda"))
listaMsg.append(MensagemNatal("Luiz"))
listaMsg.append(MensagemAniversario("Victoria"))

for msg in listaMsg:
    msg.mensagem()
