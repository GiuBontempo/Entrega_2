from classes import *
def criar_onibus():
    novo_onibus = input(f"Qual é o nome do ônibus?")
    globals()[novo_onibus] = Onibus(novo_onibus)

def criar_ponto():
    novo_ponto = input(f"Qual é o nome do ponto?")
    globals()[novo_ponto] = Ponto(novo_ponto)

def criar_motorista():
    novo_motorista = input(f"Qual é o nome do motorista?")
    globals()[novo_motorista] = Motorista(novo_motorista)

def criar_fiscal():
    novo_fiscal = input(f"Qual é o nome do fiscal?")
    globals()[novo_fiscal] = Fiscal(novo_fiscal)

def adicionar_parada():
    onibus_em_questao = input(f"A qual ônibus você deseja adiconar uma parada?")
    globals()[onibus_em_questao].adicionar_parada(globals()[input("Qual o nome da parada?")])

def ver_rota():
    onibus_em_questao = input(f"Digite o nome do ônibus do qual você quer ver a rota: ")
    print(f"{globals()[onibus_em_questao].rota}")
def troca():
    onibus_em_questao = input(f"Digite o nome do ônibus do qual você quer alterar a rota: ")
    globals()[onibus_em_questao].trocar_duas_paradas_de_lugar(globals()[input("Escolha a primeira parada para trocar de lugar: ")], globals()[input("Escolha a segunda parada para trocar de lugar: ")])
