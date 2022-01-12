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
    lista_onibus.append(globals()[novo_onibus])
    globals()[novo_onibus].motorista = globals()[novo_onibus_motorista]
    quer = input(f"Quer adicionar fiscal?\
                \n Se quer, digite: sim")
    if quer == "sim":
        novo_onibus_fiscal = input(f"Quem será o motorista do ônibus\
                                \na lista atual de motoristas é {lista_fiscais}\
                                \n")
        globals()[novo_onibus].fiscal = globals()[novo_onibus_fiscal]

def criar_ponto():
    novo_ponto = input(f"Qual é o nome do ponto?")
    globals()[novo_ponto] = Ponto(novo_ponto)
    lista_pontos.append(novo_ponto)

def criar_motorista():
    novo_motorista = input(f"Qual é o nome do motorista?")
    globals()[novo_motorista] = Motorista(novo_motorista)
    lista_motoristas.append(novo_motorista)

def criar_fiscal():
    novo_fiscal = input(f"Qual é o nome do fiscal?")
    globals()[novo_fiscal] = Fiscal(novo_fiscal)
    lista_fiscais.append(novo_fiscal)

def adicionar_parada(objeto_em_questao):
    print(f"\
           \nA atual lista de pontos é: {lista_pontos}")
    objeto_em_questao.adicionar_parada(globals()[input(f"\
                                                        \nQual o nome da parada?")])

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
         elif acao == "lista_de_onibus":
             print(f"\
                 \n A atual lista de Ônibus é {lista_onibus}")
             objeto_em_questao = globals()[input("\
                 \n Digite o nome do ônibus que você deseja alterar")]
             if objeto_em_questao in lista_onibus:
                 acao = input(f"\
                                \n Para:\
                                \nAdicionar parada, digite: adicionar_parada\
                                \n \
                                \nDeletar o ônibus, digite: deletar\
                                \n \
                                \nAlterar a rota digite: alterar_rota\
                                \n \
                                \nAlterar o motorista digite: alterar_motorista\
                                \n \
                                \nAlterar o fiscal digite: alterar_fiscal\
                                \n \
                                \nVer a tarifa digite: tarifa")
                 if acao == "adicionar_parada":
                     adicionar_parada(objeto_em_questao)
             
    elif acao == "2":
        acao = input(f"\
            \n>>>Menu Pontos<<<\
            \n \
            \n Para voltar ao Menu Central digite: menu\
            \n \
            \n Para adicionar um novo ponto digite: criar_ponto\
            \n\
            \n Para ver a lista de pontos existentes digite: lista_de_pontos\
            \n")
        if acao == "criar_ponto":
            criar_ponto()
    elif acao == "3":
        acao = input(f"\
            \n>>>Menu Motoristas<<<\
            \n \
            \n Para voltar ao Menu Central digite: menu\
            \n \
            \n Para adicionar um novo motorista digite: criar_motorista\
            \n\
            \n Para ver a lista de motoristas existentes digite: lista_de_motoristas\
            \n")
        if acao == "criar_motorista":
            criar_motorista()
    elif acao == "4":
        acao = input(f"\
            \n>>>Menu Fiscasi<<<\
            \n \
            \n Para voltar ao Menu Central digite: menu\
            \n \
            \n Para adicionar um novo fiscal digite: criar_fiscal\
            \n\
            \n Para ver a lista de fiscais existentes digite: lista_de_fiscais\
            \n")
        if acao == "criar_fiscal":
            criar_fiscal()
    acao = "menu"
        