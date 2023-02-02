import time
import concurrent.futures
from suma_prime import znajdz_sume_liczb_pierwszych

numbers = [(1,10000),(3,50000),(5000,100000),(4,900),(800,15000)]

def run_heavy_function(params):
    return znajdz_sume_liczb_pierwszych(*params)

def synchroniczna():
    start_time = time.time()
    for pair in numbers:
        prime_suma = znajdz_sume_liczb_pierwszych(*pair)
        print(prime_suma)
    end_time = time.time()
    print(f"całkowity czas policzenia sum liczb pierwszych w procesie synchronicznym: "
          f"{end_time - start_time:.2f} s")

def asynchroniczna():
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        wynik = executor.map(run_heavy_function,numbers)
    print(list(wynik))
    end_time = time.time()
    print(f"całkowity czas policzenia sum liczb pierwszych w procesie asynchronicznym: "
          f"{end_time - start_time:.2f} s")

def main():
    synchroniczna()
    asynchroniczna()

if __name__ == '__main__':
    main()
