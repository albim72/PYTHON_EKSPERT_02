from autobuilder import *

jeepBuilder = Jeep()
director = Director()
print("Samochód -> Jeep Cherokee")
director.setBuilder(jeepBuilder)
jeep = director.getCar()
jeep.specification()
print("\n")
