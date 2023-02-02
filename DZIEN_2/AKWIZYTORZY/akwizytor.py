from decimal import Decimal

class Akwizytor:
    """
    Pracownik, którego wynagrodzenie jest jedynie prowizją od sprzedaży,
    rodzaj umowy B-B
    """
    """
    komentarz niedokumentacyjny
    """
    def __init__(self,imie,nazwisko,nr_ubezpieczenia,sprzedaz,prowizja):
        self._imie = imie
        self._nazwisko = nazwisko
        self._nr_ubezpieczenia = nr_ubezpieczenia
        self.sprzedaz = sprzedaz
        self.prowizja = prowizja
        
    @property
    def imie(self):
        return  self._imie

    @property
    def nazwisko(self):
        return self.nazwisko

    @property
    def nr_ubezpieczenia(self):
        return self._nr_ubezpieczenia
    
    @imie.setter
    def imie(self,imie):
        self._imie = imie

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        self._nazwisko = nazwisko

    @nr_ubezpieczenia.setter
    def nr_ubezpieczenia(self, nr_ubezpieczenia):
        self._nr_ubezpieczenia = nr_ubezpieczenia
        
        
        
        
        
