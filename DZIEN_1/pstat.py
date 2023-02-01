liczby = [90,88,0,12,12,21,0,-78,555,-1087,2024,3100,-1088,8,23,45,111,-111,8]

def pstatystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    liczba_eleme = len(lista)
    suma = sum(lista)
    sarytm = suma/liczba_eleme
    return minimum,maksimum,rozstep,liczba_eleme,suma,sarytm

wynik = pstatystyki(liczby)
print(wynik)

mini,maxi,roz,le,sm,sar = pstatystyki(liczby)
print(f"wartość największa: {maxi}, najmniejsza: {mini}, rozstęp: {roz}, "
      f"liczba elementów: {le}, suma elementów: {sm}, średnia arytmetyczna: {sar}")
