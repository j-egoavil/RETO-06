from Shape.PointLine import Point, Line
from Shape.square import Square
from Shape.rectangle import Rectangle
from Shape.triangle import Triangle
from Shape.typeTriangle import IsoscelesTriangle, Equilateral, Scalene

if __name__ == "__main__":
   p1 = Point(1, 1)
   p2 = Point(4, 8)
   base_point1 = Point(0, 0)
   base_point2 = Point(4, 0)
   apex_point = Point(2, 3)

   print("Test Rectangle")
   rect1 = Rectangle(1, Point(0, 0), 4, 3)
   print("Method 1 -> Area:", rect1.compute_area(), "Perimeter:", rect1.compute_perimeter())

   print("\nTest Square")
   sq1 = Square(1, Point(0, 0), 4)
   print("Square -> Area:", sq1.compute_area(), "Perimeter:", sq1.compute_perimeter())

   print("\nTest Triangles")
   iso_tri = IsoscelesTriangle(base_point1, base_point2, apex_point)
   print("Isosceles angles:", iso_tri.compute_inner_angles())
   eq_tri = Equilateral(Point(0,0), Point(4,0), Point(2,3.46))
   print("Equilateral angles:", eq_tri.compute_inner_angles())
