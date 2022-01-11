lista_1 = ["c", "d"]
lista_1[0], lista_1[1] = lista_1[1], lista_1[0]
print(lista_1)
lista = ["a", "b"]
a = lista.index("a")
b = lista.index("b")
lista[a], lista[b] = lista[b], lista[a]
print(lista)