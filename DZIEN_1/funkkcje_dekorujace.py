#przykład 1
def witaj(imie):
    return f"Miło Cię widzieć {imie}"

def konkurs(imie,punkty):
    return f"uczestnik konkursu: {imie}, liczba punktów: {punkty}"

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Karol"))
print(osoba(konkurs,"Olga",78))

#przyklad 2

def startstop(funkcja):
    def wrapper(*args):
        print("Startowanie procesu:")
        funkcja(*args)
        print("Kończenie procesu....")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka")

print("_____________________________________")
zawijanie("ziemniaków")

zw = startstop(zawijanie)

zw("czekoladek")

@startstop
def dmuchanie(czego):
    print(f"dmuchanie: {czego} na urodziny.")

dmuchanie("baloników")
