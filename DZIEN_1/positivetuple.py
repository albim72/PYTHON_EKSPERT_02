#dziedziczenie typu immutable
class PositiveNumberTuple(tuple):
    def __new__(cls,*numbers):
        skipped_val = 0
        positive_numbers = []
        for x in numbers:
            if x>=0:
                positive_numbers.append(x)
            else:
                skipped_val += 1

        instance = super().__new__(cls,tuple(positive_numbers))
        instance.skipped_val = skipped_val
        return instance



pos_int_tuple = PositiveNumberTuple(-9,0,34,5,6,-7,0,12,-22,-99)
print(pos_int_tuple)
print(type(pos_int_tuple))
print(pos_int_tuple.skipped_val)

print("_____________________________________________")
def policz(a:int,b:int)->int:
    return a+2*b
print(policz)
policz2 = policz
policz8 = policz2
del policz2
def policz(a:int,b:int,c:float=.9)->float:
    return a+c*b

print(policz(2.99,True,7.6))
print(policz(2.99,True))
print(policz8(4,5))

# print(policz2 == policz)
# print(policz2)
# print(policz)

print("_____________________________________________")
