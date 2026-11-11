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

    def adicionarPostagem(self,postagem):
        self.postagens.append(postagem)

    def publicarPostagem(self, postagem):
        if postagem not in self._postagens_publicadas :
            self._postagens_publicadas.append(postagem)

    def listarPostagensPublicadas(self):
        for i,postagem in enumerate(self._postagens_publicadas):
            print(f"{i}º postagem: {postagem}")

    def listarTodasAsPostagens(self):
        for i,postagem in enumerate(self.postagens):
            print(f"{i}º postagem: {postagem}")

    def apagarPostagem(self,postagem):
        self.postagens.remove(postagem)
        if postagem in self._postagens_publicadas:
            self._postagens_publicadas.remove(postagem)
            
