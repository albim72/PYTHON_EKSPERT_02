import math

from figura import Figura

class Kolo(Figura):

    def __init__(self,a):
        super().__init__(a,0)
        del self.b

    def policz_pole(self):
        return math.pi*self.a**2

    def dwukrot(self):
        return super().dwukrot()



