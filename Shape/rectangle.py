from .shape import Shape
from .PointLine import Point

class Rectangle(Shape):
   def __init__(self, method: int, *args):
      super().__init__(is_regular = False)

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
      else:
         raise ValueError("Error: Invalid method")

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
