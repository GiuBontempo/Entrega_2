from classes import *


lista_onibus = []
lista_pontos = []
lista_motoristas = []
lista_motoristas_disponiveis = []
lista_fiscais = []
lista_fiscais_disponiveis = []

Rodando = True
acao = "menu"

def criar_onibus():
    novo_onibus = input(f"Qual é o nome do ônibus?\
                        \n")
    while True:
        novo_onibus_motorista = input(f"Quem será o motorista do ônibus\
                                    \na lista atual de motoristas disponiveis é {lista_motoristas_disponiveis}\
                                    \n")
        if globals()[novo_onibus_motorista] in lista_motoristas_disponiveis:
            globals()[novo_onibus] = Onibus(novo_onibus)
            lista_onibus.append(globals()[novo_onibus])
            globals()[novo_onibus].motorista = globals()[novo_onibus_motorista]
            lista_motoristas_disponiveis.remove(globals()[novo_onibus_motorista])
            quer = input(f"Quer adicionar fiscal?\
                        \nSe quer, digite: sim\
                        \n")
            if quer == "sim":
                while True:
                    novo_onibus_fiscal = input(f"Quem será o fiscal do ônibus\
                                            \na lista atual de fiscais disponíveis é {lista_fiscais_disponiveis}\
                                            \n")
                    if globals()[novo_onibus_fiscal] in lista_fiscais_disponiveis:
                        globals()[novo_onibus].fiscal = globals()[novo_onibus_fiscal]
                        lista_fiscais_disponiveis.remove(globals()[novo_onibus_fiscal])
                        break
                    else: print("Esse não é um fiscal disponível, tente novamente!")
                break
            break
        else:
            print("Esse não é um motorista disponível, tente novamente! (Todo ônibus precisa de um motorista)")

def criar_ponto():
    novo_ponto = input(f"Qual é o nome do ponto?\
                        \n")
    globals()[novo_ponto] = Ponto(novo_ponto)
    lista_pontos.append(globals()[novo_ponto])
    coberto = input(f"Se esse novo ponto é coberto, digite: sim\
            \n")
    if coberto == "sim":
        globals()[novo_ponto].coberto = "coberto"

def criar_motorista():
    novo_motorista = input(f"Qual é o nome do motorista?\
                            \n")
    globals()[novo_motorista] = Motorista(novo_motorista)
    lista_motoristas.append(globals()[novo_motorista])
    lista_motoristas_disponiveis.append(globals()[novo_motorista])
    sexo = input(f"Se esse novo motorista é do sexo masculino, digite: sim\
            \n")
    if sexo == "sim":
        globals()[novo_motorista].sexo = "masculino"

def criar_fiscal():
    novo_fiscal = input(f"Qual é o nome do fiscal?\
                        \n")
    globals()[novo_fiscal] = Fiscal(novo_fiscal)
    lista_fiscais.append(globals()[novo_fiscal])
    lista_fiscais_disponiveis.append(globals()[novo_fiscal])
    sexo = input(f"Se esse novo fiscal é do sexo masculino, digite: sim\
            \n")
    if sexo == "sim":
        globals()[novo_fiscal].sexo = "masculino"

def adicionar_parada(objeto_em_questao):
    print(f"\
           \nA atual lista de pontos é: {lista_pontos}\
           \nE a atual rota de {objeto_em_questao} é {objeto_em_questao.rota}")
    while True:
        p = globals()[input(f"Qual o nome da parada?\
                            \n")]
        if not p in objeto_em_questao.rota:
            objeto_em_questao.adicionar_parada(p)
            break
        else:
            print(f"O ponto {p} já está na rota do ônibus {objeto_em_questao}, tente novamente!")

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
                 \n Digite o nome do ônibus que você deseja alterar: ")]
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
                                \nVer detalhes do ônibus digite: ver\
                                \n")
                 if acao == "adicionar_parada":
                    adicionar_parada(objeto_em_questao)
                 if acao == "deletar":
                     objeto_em_questao.deletar()
                     lista_onibus.remove(objeto_em_questao)
                 elif acao == "alterar_rota":
                      print(f"\
                         \n a atual rota é: {objeto_em_questao.rota}")
                      objeto_em_questao.trocar_duas_paradas_de_lugar(globals()[input("Escolha a primeira parada para trocar de lugar: ")], globals()[input("Escolha a segunda parada para trocar de lugar: ")])
                 elif acao == "alterar_motorista":
                     while True:
                        print(f"A lista de motoristas disponíveis é {lista_motoristas_disponiveis}")
                        novo = globals()[input("Qual deve ser o novo motorista? ")]
                        if novo in lista_motoristas_disponiveis:
                            lista_motoristas_disponiveis.remove(novo)
                            lista_motoristas_disponiveis.append(objeto_em_questao.motorista)
                            objeto_em_questao.motorista = novo
                            break
                        else:
                            print("Esse não é um fiscal disponível!")
                 elif acao == "alterar_fiscal":
                     if objeto_em_questao.fiscal == "":
                         while True:
                            print(f"A lista de fiscais disponíveis é {lista_fiscais_disponiveis}")
                            novo = globals()[input("Qual deve ser o novo fiscal? ")]
                            if novo in lista_fiscais_disponiveis:
                                lista_fiscais_disponiveis.remove(novo)
                                objeto_em_questao.fiscal = novo
                                break
                            else:
                                print("Esse não é um fiscal disponível!")
                     else:
                          while True:
                            print(f"A lista de fiscais disponíveis é {lista_fiscais_disponiveis}")
                            novo = globals()[input("Qual deve ser o novo fiscal? ")]
                            if novo in lista_fiscais_disponiveis:
                                lista_fiscais_disponiveis.remove(novo)
                                lista_fiscais_disponiveis.append(objeto_em_questao.fiscal)
                                objeto_em_questao.fiscal = novo
                                break
                            else:
                                print("Esse não é um fiscal disponível!")
                 elif acao == "ver":
                     print(f"O ônibus {objeto_em_questao} possui a rota: {objeto_em_questao.rota}, é dirigido por motorista {objeto_em_questao.motorista}, e tem como fiscal {objeto_em_questao.fiscal}. Sua tarifa é de {len(objeto_em_questao.rota) * 0.2} reais")
                        
             
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
        elif acao == "lista_de_pontos":
            print(lista_pontos)
            objeto = globals()[input(f"De qual ponto você deseja tratar?\
                                        \n")]
            if objeto in lista_pontos:
                acao = input(f"Para deletar o ponto digite: deletar\
                            \nPara alterar dados do ponto digite: alterar\
                            \nPara ver os dados do ponto digite: ver\
                            \n")
                if acao == "deletar":
                        objeto.deletar()
                        lista_pontos.remove(objeto)
                if acao == "alterar":
                    objeto.coberto = input("Digite coberto caso o ponto seja coberto, ou descoberto caso o ponto seja descoberto: ")
                if acao == "ver":
                    print(f"O ponto {objeto} é {objeto.coberto}")

                        
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
        if acao == "lista_de_motoristas":
            print(lista_motoristas)
            objeto = globals()[input(f"De qual motorista você deseja tratar?\
                                        \n")]
            if objeto in lista_motoristas:
                acao = input(f"Para deletar o motorista digite: deletar\
                            \nPara alterar dados do motorista digite: alterar\
                            \nPara ver os dados do motorista digite: ver\
                            \n")
                if acao == "deletar":
                        objeto.deletar()
                        lista_motoristas.remove(objeto)
                        lista_motoristas_disponiveis.remove(objeto)
                if acao == "alterar":
                    objeto.sexo = input("Digite o sexo do motorista: ")
                if acao == "ver":
                    print(f"{objeto} é do sexo {objeto.sexo}")



    elif acao == "4":
        acao = input(f"\
            \n>>>Menu Fiscais<<<\
            \n \
            \n Para voltar ao Menu Central digite: menu\
            \n \
            \n Para adicionar um novo fiscal digite: criar_fiscal\
            \n\
            \n Para ver a lista de fiscais existentes digite: lista_de_fiscais\
            \n")
        if acao == "criar_fiscal":
            criar_fiscal()
        if acao == "lista_de_fiscais":
            print(lista_fiscais)
            objeto = globals()[input(f"De qual fiscal você deseja tratar?\
                                        \n")]
            if objeto in lista_fiscais:
                acao = input(f"Para deletar o fiscal digite: deletar\
                            \nPara alterar dados do fiscal digite: alterar\
                            \nPara ver os dados do fiscal digite: ver\
                            \n")
                if acao == "deletar":
                        objeto_em_questao.deletar()
                        lista_fiscais.remove(objeto)
                        lista_fiscais_disponiveis.remove(objeto)
                if acao == "alterar":
                    objeto.sexo = input("Digite o sexo do fiscal: ")
                if acao == "ver":
                    print(f"{objeto} é do sexo {objeto.sexo}")
    acao = "menu"
