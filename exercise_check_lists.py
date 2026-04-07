# Ejercicio 11: Comparar tercer elemento de dos listas

def check_lists(lista1, lista2):
    if len(lista1) > 2 and len(lista2) > 2 and lista1[2] == lista2[2]:
        print("true")
        return "true"
    else:
        print("false")
        return "false"