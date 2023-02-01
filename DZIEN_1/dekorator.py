import time
import math


def pomiarczasu(funkcja):
    def wrapper():
        print(f'wołana funkcja: {funkcja.__name__}')
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f"czas wykonania funckji: {endtime - starttime} s")
    return wrapper

def nazwaf(funkcja):
    def wrapper(*args):
        print(f'wołana funckja: {funkcja.__name__}')
    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper



@sleep
@pomiarczasu
def big_lista():
    sum([i**2 for i in range(10000000)])

big_lista()

