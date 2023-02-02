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
        print(id(self.sprzedaz))
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

    @property
    def sprzedaz(self):
        return self._sprzedaz

    @sprzedaz.setter
    def sprzedaz(self,kwota):
        if kwota<Decimal('0.00'):
            raise ValueError('Wartość sprzedaży nie może być mnieja od zera.')
        self._sprzedaz = kwota

    @property
    def prowizja(self):
        return self._prowizja

    @prowizja.setter
    def prowizja(self, procent):
        if not(Decimal('0.00')<procent<Decimal('30.0')):
            raise ValueError('Prowizja od sprzedaży zawiera się 0-30.')
        self._prowizja = procent


    def zarobek(self):
        return self.sprzedaz*(self.prowizja/Decimal('100.0'))

    def __repr__(self):
        """reprezentacja tekstowa obiektu"""
        return (f'Akwizytor: {self.imie} {self.nazwisko}\n'
                f'numer ubezpieczenia: {self.nr_ubezpieczenia}\n'
                f'sprzedaż: {self.sprzedaz:.2f} zł\n'
                f'prowizja: {self.prowizja:.2f} zł\n')




