import math
from NegativeAError import NegAError

#założenie a nie może być ujemna
def gx(a,b):
    if a<0:
        raise NegAError(a)
    try:
        wynik =  a*math.sqrt(b)
    except ValueError as ve:
        return f'{ve} -> wartość podpierwiastkowa b nie być ujemna'
    else:
        return wynik

# def gx(a,b):
#     if a<0:
#         raise NegAError(a)
#     wynik =  a*math.sqrt(b)
#     return wynik

try:
    print(gx(3,4))
    print(gx(-3, 6))
    print(gx(3,-2))
except NegAError as me:
    print(me)
