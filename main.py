from classes import *

carro=onibus("carro")
cachoeira=Ponto("cachoeira")
lagoa=Ponto("lagoa")
carro.adicionar_parada(cachoeira)
carro.adicionar_parada(lagoa)
print (carro.rota)