print("Este programa suma los dos numeros mas altos en una lista")

def suma_numeros_mas_altos(numeros):

    if not numeros:
        print("Error: la lista está vacía.")
        return
    
    if len(numeros) < 2:
        print("Error: se necesitan al menos dos números para realizar la suma.")
        return

    # Ordenar la lista en orden ascendente
    numeros.sort()
    
    # Sumar los dos últimos (los más grandes)
    resultado = numeros[-1] + numeros[-2]
    print(f"El resultado de sumar los dos números más grandes es: {resultado}")


try:
    entrada = input("Introduce una lista de números separados por comas: ").strip()

    if not entrada:
        print("Error: no ingresaste ningún número.")
    else:
        # Convertir la entrada en lista de enteros
        lista_numeros = [int(x.strip()) for x in entrada.split(",")]
        suma_numeros_mas_altos(lista_numeros)

except ValueError:
    print("Error: asegúrate de ingresar solo números separados por comas (ejemplo: 5, 8, 12, 3).")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

"""
explicacion

le pedimos al usuario que inserte una lista de numeros
luego ordenaremos la lista y sumeremos los dos ultimos numeros que deberan ser los mas grandes
"""