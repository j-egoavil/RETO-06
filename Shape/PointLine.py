class Point:
   def __init__(self, x: float, y: float) -> None:
      self._x = x
      self._y = y

class Line(Point):
   def __init__(self, start: Point, end: Point ) -> None:
      super().__init__(start._x, start._y)
      self._start = start
      self._end = end

   def compute_length(self) -> float:
      length = ((self._end._x - self._start._x) ** 2 + (self._end._y - self._start._y) ** 2) ** 0.5
      return length
    
   def compute_slope(self):
      if (self._end._x - self._start._x) == 0:
         return None  
      slope: float = (self._end._y - self._start._y) / (self._end._x - self._start._x)
      return slope
    
   def compute_vertical_crossing(self):
      slope = self.compute_slope()
      if slope is None:
         return None
      crossing = self._start._y - (slope * self._start._x)
      return crossing

   def compute_horizontal_crossing(self):
      slope = self.compute_slope()
      if slope == 0 or slope is None:
         return None
      crossing = -(self._start._y - (slope * self._start._x)) / slope
      return crossing
    
   def __str__(self) -> str:
      slope = self.compute_slope()
      slope_str = f"{slope:.2f}" if slope is not None else "Undefined"
      v_cross = self.compute_vertical_crossing()
      h_cross = self.compute_horizontal_crossing()
      return (
         f"Length: {self.compute_length():.2f}, "
         f"Slope: {slope_str}, "
         f"Vertical crossing: {v_cross}, "
         f"Horizontal crossing: {h_cross}"
        )
