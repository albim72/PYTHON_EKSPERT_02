class MojaMeta(type):
    def __new__(cls, clsname,supercls,attrdict):
        print(f"nazwa klasy: {clsname}")
        print(f"dziedziczone klasy: {supercls}")
        print(f"słownik atrybutów: {attrdict}")
        return type.__new__(cls, clsname,supercls,attrdict)


class Basic:
    pass

b = Basic()


class Pochodna(Basic,metaclass=MojaMeta):
    pass

class Druga(Pochodna):
    pass

class X:
    pass

class Y:
    pass

class Trzecia(X,Y,Druga):
    pass
