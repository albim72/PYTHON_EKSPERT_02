#przykład 1
def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik konkursu: {imie}, liczba punktów: {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Karol"))
print(osoba(konkurs,"Olga",78))
