class NegAError(Exception):
    def __init__(self,a):
        self.a = a
    def __str__(self):
        return f'wartość a = {self.a} nie może być ujemna'
