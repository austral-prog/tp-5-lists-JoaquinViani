# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    if indice >= len(lista) or indice <= len(lista):
        return None
    return lista[indice]
