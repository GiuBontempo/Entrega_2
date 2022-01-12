from classes import *


lista_onibus = []
lista_pontos = []
lista_motoristas = []
lista_fiscais = []

Rodando = True
acao = "menu"

def criar_onibus():
    novo_onibus = input(f"Qual é o nome do ônibus?\
                        \n")
    novo_onibus_motorista = input(f"Quem será o motorista do ônibus\
                                \na lista atual de motoristas é {lista_motoristas}\
                                \n")
    globals()[novo_onibus] = Onibus(novo_onibus)
    lista_onibus.append(novo_onibus)
    globals()[novo_onibus].fiscal = globals()[novo_onibus_fiscal]
    quer = input(f"Quer adicionar fiscal?\
                \n Se quer, digite: sim")
    if quer == "sim":
        novo_onibus_fiscal = input(f"Quem será o motorista do ônibus\
                                \na lista atual de motoristas é {fiscais}\
                                \n")
        globals()[novo_onibus].fiscal = globals()[novo_onibus_fiscal]

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


while Rodando:
    if acao == "menu":
        acao = input(f"\
            \n>>>Menu central<<<\
            \n \
            \nPara acessar o menu Ônibus, digite: 1\
            \n \
            \nPara acessar o menu Pontos, digite: 2\
            \n \
            \nPara acessar o menu Motoristas, digite: 3\
            \n \
            \nPara acessar o menu Fiscais, digite: 4\
            \n \
            \nPara fechar o programa, digite: sair\
            \n")
    if acao== "sair":
        Rodando = False
    elif acao == "1":
         acao = input(f"\
            \n>>>Menu Ônibus<<<\
            \n \
            \n Para voltar ao Menu Central digite: menu\
            \n \
            \n Para adicionar um novo Ônibus digite: criar_onibus\
            \n\
            \n Para ver a lista de Ônibus existentes digite: lista_de_onibus\
            \n")
         if acao == "criar_onibus":
                criar_onibus()
    elif acao == "2":
        pass
    elif acao == "3":
        pass
    elif acao == "4":
        pass
        