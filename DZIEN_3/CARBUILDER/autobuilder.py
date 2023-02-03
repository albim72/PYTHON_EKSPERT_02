from abc import ABC, abstractmethod

class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None

class Car:
    def __init__(self):
        self._wheels = list()
        self._engine = None
        self._body = None

    def setBody(self,body):
        self._body = body

    def setEngine(self,engine):
        self._engine = engine

    def attachWheel(self,wheel):
        self._wheels.append(wheel)

    def specification(self):
        print(f'rodzaj pojazdu: {self._body.shape}')
        print(f'silnik [kM]: {self._engine.horsepower}')
        print(f'średnica koła [cal]: {self._wheels[0].size}')
        
#Bulider
class Builder(ABC):
    @abstractmethod
    def getWheel(self):pass

    @abstractmethod
    def getEngine(self): pass

    @abstractmethod
    def getBody(self): pass
    
#Director

