from figura import Figura

class Trojkat(Figura):
    def policz_pole(self):
        return self.a*self.b/2

    def dwukrot(self):
        return super().dwukrot()
