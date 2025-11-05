print("Este programa revisa si una palabra o frase es un palindromo o no")

def palindromo(palabra:str):
    try:
        # Validar entrada vacía
        if not palabra.strip():
            print("Error: la cadena está vacía.")
            return

        # Convertir a minúsculas y eliminar espacios
        palabra = palabra.lower().replace(" ", "")
        resultado = ""

        # Invertir la palabra
        for letra in palabra:
            resultado = letra + resultado

        # Comparar palabra original con la invertida
        if palabra == resultado:
            print("La palabra o frase ES un palíndromo.")
        else:
            print("La palabra o frase NO es un palíndromo.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


# Solicitar entrada al usuario
palabra = input("Ingresa la palabra o frase a revisar: ")

# Llamar a la función
palindromo(palabra)
"""
explicacion

Se toma la palabra del usuario y se escribe en minúsculas.
Luego, se invierte usando una cadena vacía para mostrar el resultado. 
Se realiza una comparación para ver si esa palabra es igual a la original.
"""