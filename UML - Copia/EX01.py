from datetime import datetime


class Usuario:
    def __init__(self, id: int, nome: str, login: str, senha: str):
        self._id = id
        self._nome = nome
        self._login = login
        self._senha = senha
        self._autenticado = False

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def login(self):
        return self._login

    @property
    def senha(self):
        return self._senha

    @property
    def autenticado(self):
        return self._autenticado

    def autenticar(self, login: str, senha: str):
        if self._login == login and self._senha == senha:
            self._autenticado = True
            return True

        self._autenticado = False
        return False

    def deslogar(self):
        self._autenticado = False

    def __str__(self):
        return f"{self._nome} (@{self._login})"


class Postagem:
    def __init__(
        self,
        id: int,
        titulo: str,
        texto: str,
        dataPublicacao: datetime,
        usuario: Usuario,
    ):
        self._id = id
        self._titulo = titulo
        self._texto = texto
        self._dataPublicacao = dataPublicacao
        self._usuario = usuario

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def texto(self):
        return self._texto

    @property
    def dataPublicacao(self):
        return self._dataPublicacao

    @property
    def usuario(self):
        return self._usuario

    def __str__(self):
        return f"{self._titulo} - {self._usuario} - {self._dataPublicacao.strftime('%d/%m/%Y')}"


class Blog:
    def __init__(self):
        self._postagens = []
        self._postagens_publicadas = []

    @property
    def postagens(self):
        return self._postagens

    @postagens.setter
    def postagens(self, postagens):
        self._postagens = postagens

    @property
    def postagens_publicadas(self):
        return self._postagens_publicadas

    def adicionarPostagem(self, usuario: Usuario, postagem: Postagem):
        if not isinstance(usuario, Usuario):
            raise TypeError("O usuário informado não é válido.")

        if not usuario.autenticado:
            raise PermissionError(
                "Para criar uma postagem, o usuário precisa estar autenticado."
            )

        if postagem.usuario is not usuario:
            raise ValueError("A postagem deve registrar o usuário que a criou.")

        self._postagens.append(postagem)
        self.publicarPostagem(postagem)

    def criarPostagem(
        self,
        usuario: Usuario,
        id: int,
        titulo: str,
        texto: str,
        dataPublicacao: datetime,
    ):
        postagem = Postagem(id, titulo, texto, dataPublicacao, usuario)
        self.adicionarPostagem(usuario, postagem)
        return postagem

    def publicarPostagem(self, postagem: Postagem):
        if (
            postagem not in self._postagens_publicadas
            and postagem.dataPublicacao <= datetime.now()
        ):
            self._postagens_publicadas.append(postagem)

    def listarPostagensPublicadas(self):
        publicadas = [
            postagem
            for postagem in self._postagens
            if postagem.dataPublicacao <= datetime.now()
        ]
        if not publicadas:
            print("Nenhuma postagem publicada até o momento.")
            return

        for i, postagem in enumerate(publicadas, start=1):
            print(f"{i}º postagem: {postagem}")

    def listarTodasAsPostagens(self):
        if not self._postagens:
            print("Nenhuma postagem cadastrada.")
            return

        for i, postagem in enumerate(self.postagens, start=1):
            print(f"{i}º postagem: {postagem}")

    def apagarPostagem(self, postagem: Postagem):
        if postagem in self.postagens:
            self.postagens.remove(postagem)
        if postagem in self._postagens_publicadas:
            self._postagens_publicadas.remove(postagem)


if __name__ == "__main__":
    usuario = Usuario(1, "Maria", "maria", "1234")
    usuario.autenticar("maria", "1234")

    blog = Blog()
    blog.criarPostagem(
        usuario,
        1,
        "Primeiro post",
        "Texto da postagem publicada.",
        datetime(2025, 1, 1),
    )

    blog.criarPostagem(
        usuario,
        2,
        "Post futuro",
        "Este post ainda não pode ser visto publicamente.",
        datetime(2030, 1, 1),
    )

    print("Postagens publicadas:")
    blog.listarPostagensPublicadas()

    print("\nTodas as postagens:")
    blog.listarTodasAsPostagens()
