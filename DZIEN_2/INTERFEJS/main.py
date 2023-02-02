from Pojazd import Pojazd

p1 = Pojazd()

lt = 56
odl = 670
cena_l = 7.82
print(f'spalanie na l/100km: {p1.spalanie_100(odl, lt):.2f}')

print(f'koszt przejazdu na trasie: {odl} km wynosi {p1.kosztprzejazdu(odl,lt,cena_l):.2f} zł')
