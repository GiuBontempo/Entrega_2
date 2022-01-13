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
        self.coberto = "descoberto"


class Motorista(dado):
    def __init__(self, nome):
        super().__init__(nome)
        self.sexo = "feminino"


class Fiscal(dado):
    def __init__(self, nome):
        super().__init__(nome)
        self.sexo = "feminino"


class Onibus(dado):
    def __init__(self, nome):
        super().__init__(nome)
        self.rota = []
        self.motorista = ""
        self.fiscal = ""

    def adicionar_parada(self, ponto = Ponto):
        if not ponto in self.rota:
            self.rota.append(ponto)
        else: print(f"Essa parada já está na rota do ônibus")

    def adicionar_motorista(self, motorista = Motorista):
        self.fiscal.append(motorista)

    def adicionar_fiscal(self, fiscal = Fiscal):
        self.fiscal.append(fiscal)

    def trocar_duas_paradas_de_lugar(self, primeira_parada, segunda_parada):
        while True:
            if primeira_parada in self.rota:
                if segunda_parada in self.rota:
                    a = self.rota.index(primeira_parada)
                    b = self.rota.index(segunda_parada)
                    self.rota[a], self.rota[b] = self.rota[b], self.rota[a]
                    break
                else: segunda_parada = input(f"A parada {segunda_parada} não está na rota desse ônibus, escolha outra parada.")
            else: primeira_parada = input(f"A parada {primeira_parada} não está na rota desse ônibus, escolha outra parada.")
