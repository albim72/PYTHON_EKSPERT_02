
#przykład 1
def liczby():
    for i in range(16):
        yield i

for p in liczby():
    print(p)
