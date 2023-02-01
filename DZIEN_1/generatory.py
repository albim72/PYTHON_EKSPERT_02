
#przykład 1
def liczby():
    for i in range(16):
        yield i

for p in liczby():
    print(p)

#przykład 2

def wznowienie(n,k):
    print("wstrzymanie działania")
    yield 1001
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n+k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n-k
    print("wznowienie działania")

    print("wstrzymanie działania")
    yield n*k
    print("wznowienie działania")

for i in wznowienie(6,4):
    if i==1001:
        continue
    print(f"zwrócono wartość: {i}")

#przykład 3

def genret():
    for i in range(9):
        if i==6:
            print("przerwanie")
            return
        else:
            yield i


for t in genret():
    print(t)
