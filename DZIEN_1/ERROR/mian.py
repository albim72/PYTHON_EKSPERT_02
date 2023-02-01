import math

#założenie a nie może być ujemna
def gx(a,b):
    try:
        wynik =  a*math.sqrt(b)
    except ValueError as ve:
        return f'{ve} -> wartość podpierwiastkowa b nie być ujemna'
    else:
        return wynik

print(gx(3,4))
print(gx(3,-2))
print(gx(-3,6))
