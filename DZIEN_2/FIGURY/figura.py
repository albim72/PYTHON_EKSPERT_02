from abc import ABC,abstractmethod

class Figura(ABC):
    def __init__(self,a,b):
        self.a = a
        self.b =b
        self.cr_figura()

    def cr_figura(self):
        print("utworzono nową figurę płaską...")

    @abstractmethod
    def policz_pole(self):
        pass

    @abstractmethod
    def dwukrot(self):
        return self.a*2

