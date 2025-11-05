print("Este programa hace operaciones basicas")


def calcular(num_1:float, num_2:float, operacion:str):
      if operacion == "+":
        return num_1 + num_2
      elif operacion == "-":
        return num_1 - num_2
      elif operacion == "*":
        return num_1 * num_2
      elif operacion == "/":
        if num_2 == 0:
            return "Error: No se puede dividir entre cero."
        return num_1 / num_2
      else:
        return "Error: Operación no válida. Use +, -, * o /."
     
try:
    num_1 = float(input("Ingrese el primer número (puede tener decimales): "))
    num_2 = float(input("Ingrese el segundo número (puede tener decimales): "))
    operacion = input("Ingrese la operación que desea realizar (+, -, *, /): ")

    resultado = calcular(num_1, num_2, operacion)
    print(f"\nResultado: {resultado}")

except ValueError:
    print("Error: Ingrese solo números válidos.")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

""" 
explicacion

Se toman los dos números y la operación, y la operación a realizar se define según la 
entrada del usuario. Devuelve el valor de esa operación.
"""