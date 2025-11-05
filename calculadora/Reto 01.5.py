print("Este programa encuentra palabras que son anagramas ")


def filtrar_anagramas(lista):

    if not lista:
        print("Error: la lista está vacía.")
        return []

    # Filtrar palabras vacías (por si el usuario pone comas seguidas)
    lista = [palabra.strip() for palabra in lista if palabra.strip()]
    if not lista:
        print("Error: no se ingresaron palabras válidas.")
        return []

    # Crear un diccionario para agrupar anagramas
    grupos = {}
    for palabra in lista:
        clave = "".join(sorted(palabra.lower()))
        if clave in grupos:
            grupos[clave].append(palabra)
        else:
            grupos[clave] = [palabra]

    # Extraer solo los grupos con más de una palabra
    resultado = []
    for grupo in grupos.values():
        if len(grupo) > 1:
            resultado.extend(grupo)

    if resultado:
        print("Palabras que son anagramas:", resultado)
    else:
        print("No se encontraron anagramas.")
    return resultado


try:
    entrada = input("Introduce palabras separadas por comas: ").strip()

    if not entrada:
        print("Error: no ingresaste ninguna palabra.")
    else:
        palabras = [p.strip() for p in entrada.split(",")]
        filtrar_anagramas(palabras)

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
"""
explicacion

se crea un diccionario vacio en el cual se van a ir ingrasando las claves
que son las palabras organizadas para luego comparar con el resto de palabras
para revisar si son anagramas
"""