# Ejercicio 10: Concatenar listas

def concatenate_lists(lista1, lista2):
    lista1 = lista1 + lista2
    print(lista1)

concatenate_lists([1, 2, 3], [4, 5, 6])
concatenate_lists([], [1, 2, 3])
concatenate_lists([1, 2], ["a", "b"])