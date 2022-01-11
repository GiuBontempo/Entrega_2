class dado:
    def __init__(self, nome = str):
        self.nome = nome

    def deletar(self):
        print(f"{self.nome} deletado")
        del self

    def __str__(self):
        return f"{self.nome}"

    __repr__ = __str__


class Ponto(dado):
    def __init__(self, nome):
        super().__init__(nome)


class onibus(dado):
    def __init__(self, nome):
        super().__init__(nome)
        self.rota = []
        self.motorista = ""
        self.fiscal = ""



    def adicionar_parada(self, ponto = Ponto):
        self.rota.append(ponto)