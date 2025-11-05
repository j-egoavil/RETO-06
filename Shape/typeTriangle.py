from math import pi, acos
from .triangle import Triangle
from .PointLine import Point

class IsoscelesTriangle(Triangle):
   def __init__(self, base_point1: Point, base_point2: Point, apex_point: Point):
      self.is_regular = False
      super().__init__(base_point1, base_point2, apex_point)
      if not (self.edges[0].compute_length() == self.edges[1].compute_length() or
               self.edges[1].compute_length() == self.edges[2].compute_length() or
               self.edges[0].compute_length() == self.edges[2].compute_length()):
            raise ValueError("Error: The provided points do not form an isosceles triangle")
    
   def compute_inner_angles(self):
      if self.edges[0].compute_length() == self.edges[1].compute_length():
            a = self.edges[0].compute_length()
            b = self.edges[2].compute_length()
      elif self.edges[1].compute_length() == self.edges[2].compute_length():
            a = self.edges[1].compute_length()
            b = self.edges[0].compute_length() 
      else:
            a = self.edges[0].compute_length()
            b = self.edges[1].compute_length()

      test = (b/2)/a
      angle1 = acos(test) * (180 / pi)
      angle2 = angle1
      angle3 = 180 - 2 * angle1
      return angle1, angle2, angle3
    
class Equilateral(Triangle):
   def __init__(self, p_e1: Point, p_e2: Point, p_e3: Point):
      self.is_regular = True
      super().__init__(p_e1, p_e2, p_e3)
    
   def compute_inner_angles(self):
      return 60, 60, 60
        
class Scalene(Triangle):
   def __init__(self, p_s1: Point, p_s2: Point, p_s3: Point):
      self.is_regular = False
      super().__init__(p_s1, p_s2, p_s3)
      if (self.edges[0].compute_length() == self.edges[1].compute_length() or
         self.edges[1].compute_length() == self.edges[2].compute_length() or
         self.edges[0].compute_length() == self.edges[2].compute_length()):
         raise ValueError("Error: The provided points do not form a scalene triangle")
    
   def compute_inner_angles(self):
      a = self.edges[0].compute_length()
      b = self.edges[1].compute_length()
      c = self.edges[2].compute_length()

      angle1 = acos((b**2 + c**2 - a**2) / (2 * b * c)) * (180 / pi)
      angle2 = acos((a**2 + c**2 - b**2) / (2 * a * c)) * (180 / pi)
      angle3 = 180 - angle1 - angle2
      return angle1, angle2, angle3
