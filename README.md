# RETO-06
This repository contains documented and explained practical exercises in OOP in Python.

---

## In the package Shape identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.
**In this case, 3 exceptions were added to the square class.**

### `main.py`
```python
from area_perimeter.point import Point
from area_perimeter.line import Line
from area_perimeter.rectangle import Rectangle
from area_perimeter.square import Square
from area_perimeter.triangle import Triangle
from area_perimeter.isosceles import IsoscelesTriangle
from area_perimeter.equilateral import Equilateral
from area_perimeter.scalene import Scalene

def main():
    # Points
    p1 = Point(0, 0)
    p2 = Point(3, 4)

    # Rectangles
    rect = Rectangle(1, p1, 10, 5)
    print(f"Rectángulo: área = {rect.compute_area()}, perímetro = {rect.compute_perimeter()}")

    # Squares
    sq = Square(1, p1, 5)
    print(f"Cuadrado: área = {sq.compute_area()}, perímetro = {sq.compute_perimeter()}")

    # Traingles
    t = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))
    print(f"Triángulo: área = {t.compute_area()}, perímetro = {t.compute_perimeter()}")

    iso = IsoscelesTriangle(Point(0, 0), Point(4, 0), Point(2, 3))
    print(f"Triángulo isósceles: área = {iso.compute_area()}, perímetro = {iso.compute_perimeter()}")

    scal = Scalene(Point(0, 0), Point(4, 0), Point(3, 2))
    print(f"Triángulo escaleno: área = {scal.compute_area()}, perímetro = {scal.compute_perimeter()}")

    equi = Equilateral(Point(0, 0), Point(4, 0), Point(2, 3.46))
    print(f"Triángulo equilátero: área = {equi.compute_area()}, perímetro = {equi.compute_perimeter()}")

if __name__ == "__main__":
    main()

```
### `__init__.py`
```python
from .point import Point
from .line import Line
from .shape import Shape
from .rectangle import Rectangle
from .square import Square
from .triangle import Triangle
from .isosceles import IsoscelesTriangle
from .equilateral import Equilateral
from .scalene import Scalene

```
### `shape.py`
```python
class Shape:
    def __init__(self, is_regular: bool):
        self.is_regular = is_regular
        self.vertices: list = []
        self.edges: list = []

    def compute_area(self):
        return 0
    
    def compute_perimeter(self):
        if not self.edges:
            return 0
        return sum(edge.compute_length() for edge in self.edges)
    
    def inner_angle(self, sides: int) -> float:
        if sides < 3:
            return 0
        return (sides - 2) * 180 / sides
    
    def compute_inner_angles(self):
        sides = len(self.vertices)
        if sides < 3:
            return 0
        return (sides - 2) * 180

```

### `point.py`
```python
class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y

```
### `line.py`
```python
from math import sqrt
from Reto_06.point import Point

class Line(Point):
    def __init__(self, start: Point, end: Point) -> None:
        super().__init__(start._x, start._y)
        self._start = start
        self._end = end

    def compute_length(self) -> float:
        return sqrt((self._end._x - self._start._x) ** 2 + (self._end._y - self._start._y) ** 2)
    
    def compute_slope(self):
        if (self._end._x - self._start._x) == 0:
            return None
        return (self._end._y - self._start._y) / (self._end._x - self._start._x)
    
    def compute_vertical_crossing(self):
        slope = self.compute_slope()
        if slope is None:
            return None
        return self._start._y - (slope * self._start._x)

    def compute_horizontal_crossing(self):
        slope = self.compute_slope()
        if slope == 0 or slope is None:
            return None
        return -(self._start._y - (slope * self._start._x)) / slope
    
    def __str__(self) -> str:
        slope = self.compute_slope()
        slope_str = f"{slope:.2f}" if slope is not None else "∞"
        v_cross = self.compute_vertical_crossing()
        h_cross = self.compute_horizontal_crossing()
        return (
            f"Length: {self.compute_length():.2f}, "
            f"Slope: {slope_str}, "
            f"Vertical crossing: {v_cross}, "
            f"Horizontal crossing: {h_cross}"
        )

```
### `rectangle.py`
```python
from area_perimeter.shape import Shape
from area_perimeter.point import Point

class Rectangle(Shape):
    def __init__(self, method: int, *args):
        super().__init__(is_regular=False)

        if method == 1:
            bottom_left, width, height = args
            self.width = width
            self.height = height
            self.center = Point(bottom_left._x + width/2, bottom_left._y + height/2)

        elif method == 2:
            center, width, height = args
            self.width = width
            self.height = height
            self.center = center

        elif method == 3:
            p1, p2 = args
            self.width = abs(p2._x - p1._x)
            self.height = abs(p2._y - p1._y)
            self.center = Point((p1._x + p2._x)/2, (p1._y + p2._y)/2)

        elif method == 4:
            lines = args
            points = [p for line in lines for p in (line._start, line._end)]
            xs, ys = [p._x for p in points], [p._y for p in points]
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)
            self.width = max_x - min_x
            self.height = max_y - min_y
            self.center = Point((min_x + max_x)/2, (min_y + max_y)/2)
        else:
            raise ValueError("Invalid method")

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def compute_interference_point(self, point: Point) -> bool:
        x_min = self.center._x - self.width/2
        x_max = self.center._x + self.width/2
        y_min = self.center._y - self.height/2
        y_max = self.center._y + self.height/2
        return x_min <= point._x <= x_max and y_min <= point._y <= y_max

```
### `square.py`
```python
from area_perimeter.rectangle import Rectangle
from area_perimeter.point import Point

class Square(Rectangle):
    def __init__(self, method: int, *args):
        # Exception: invalid method
        if method not in (1, 2, 3):
            raise ValueError(f"Invalid method '{method}'. Must be 1, 2, or 3.")

        # Exception: invalid number of arguments
        if (method in (1, 2) and len(args) != 2) or (method == 3 and len(args) != 2):
            raise TypeError(
                f"Invalid number of arguments for method {method}. Expected 2, got {len(args)}."
            )
        
        # Exception: first argument must be a Point
        if not isinstance(args[0], Point):
            raise TypeError("The first argument must be an instance of Point.")
        if method == 1:
            bottom_left, side = args
            super().__init__(1, bottom_left, side, side)
        elif method == 2:
            center, side = args
            super().__init__(2, center, side, side)
        elif method == 3:
            p1, p2 = args
            side = max(abs(p2._x - p1._x), abs(p2._y - p1._y))
            center = Point((p1._x + p2._x)/2, (p1._y + p2._y)/2)
            super().__init__(2, center, side, side)
        else:
            raise ValueError("Invalid method")

```
### `triangle.py`
```python
from .shape import Shape
from .line import Line
from .point import Point
import math

class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(is_regular=False)
        self.vertices = [p1, p2, p3]
        self.edges = [
            Line(p1, p2),
            Line(p2, p3),
            Line(p3, p1)
        ]

    def compute_perimeter(self):
        return sum(edge.compute_length() for edge in self.edges)

    def compute_area(self):
        a, b, c = [edge.compute_length() for edge in self.edges]
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Fórmula de Herón

    def compute_inner_angles(self):
        a, b, c = [edge.compute_length() for edge in self.edges]
        A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
        B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
        C = 180 - A - B
        return A, B, C

```
### `isosceles.py`
```python
from .triangle import Triangle
from .line import Line
from .point import Point
import math

class IsoscelesTriangle(Triangle):
    def __init__(self, base_start: Point, base_end: Point, vertex: Point):
        super().__init__(base_start, base_end, vertex)
        self.is_regular = False

    def compute_area(self):
        base_length = self.edges[0].compute_length()
        side_length = self.edges[1].compute_length()
        h = (side_length ** 2 - (base_length ** 2) / 4) ** 0.5
        return (base_length * h) / 2

```
### `scalene.py`
```python
from .triangle import Triangle

class Scalene(Triangle):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        self.is_regular = False

```
### `equilateral.py`
```python
from .triangle import Triangle
from .point import Point
import math

class Equilateral(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self.is_regular = True

    def compute_area(self):
        side = self.edges[0].compute_length()
        return (math.sqrt(3) / 4) * (side ** 2)

    def compute_perimeter(self):
        side = self.edges[0].compute_length()
        return 3 * side

    def compute_inner_angles(self):
        return (60.0, 60.0, 60.0)

```

## Add the required exceptions in the Reto 1 code assigments.

### `exercise_1.py` -> Calculator
```python
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
```
### `exercise_2.py` -> Palindrome
```python
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
```
### `exercise_3.py` -> Prime numbers
```python
print("este programa revisa si un numero es primo")


def es_primo(numero):
    # el primo menor es 2 por lo que culaquier numero anterior no lo es
    if numero < 2:
        return False
    # calcula si el numero es primo o no 
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


# crea una lista con los numeros que sean primos
def filtrar_primos(lista):
    if not lista:
        print("Error: la lista está vacía.")
        return []

    primos = [num for num in lista if es_primo(num)]

    if primos:
        print("Números primos encontrados:", primos)
    else:
        print("No se encontraron números primos en la lista.")
    return primos


try:
    entrada = input("Introduce una lista de números separados por comas: ").strip()

    if not entrada:
        print("Error: no ingresaste ningún número.")
    else:
        lista_numeros = [int(x.strip()) for x in entrada.split(",")]
        filtrar_primos(lista_numeros)

except ValueError:
    print("Error: asegúrate de ingresar solo números separados por comas (ejemplo: 2, 3, 5, 8).")

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
```
### `exercise_4.py` -> Greater sum
```python
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
```
### `exercise_5.py` -> Anagram
```python
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
```
