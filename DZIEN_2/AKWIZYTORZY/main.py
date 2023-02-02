from decimal import Decimal
from akwizytor import Akwizytor
from akwizytornaetacie import AkwizytorNaEtacie

class Firma:
    def __repr__(self):
        return 'Jestem szefem i właścicielem ustala roczną dywidendę na 1 mln zł'

    def zarobek(self):
        return Decimal('1_000_000.00')

k = Firma()
s = AkwizytorNaEtacie("Tomek","Kot","5532353455-T",Decimal('256900'),Decimal('3.7'),Decimal('5500'))
c = Akwizytor("Olga","Nowak","5537688785-T",Decimal('516700'),Decimal('4.4'))

pracownicy = [c,s,k]

for pr in pracownicy:
    print(pr)
    print(f'{pr.zarobek():,.2f} zł\n')


ak = Akwizytor("Olga","Kowal","553744785-T",Decimal('111700'),Decimal('6.4'))

print(id(ak.sprzedaz))
print(id(ak._sprzedaz))
