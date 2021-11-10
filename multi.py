from threading import Thread
from numba import jit
from numba.typed import List
import time


def find_prime_number_from_order(n):
    i = 1
    x = 2
    while i < n:
        x = next_prime_number(x)
        i += 1
        print(f"{i} / {n} = {x}")
    return x


def next_prime_number(x):
    while True:
        x += 1
        i = 2
        n = 4
        divider_init = [False for _ in range(n)]
        divider = List()
        [divider.append(x) for x in divider_init]
        threads = [Thread(target=check_divider, args=(i+j, x, n, j, divider)) for j in range(n)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        if not any(divider):
            break
    return x


@jit(nopython=True, nogil=True)
def check_divider(i, x, d, index, divider):
    divider[index] = False
    while i < x:
        if x % i == 0:
            divider[index] = True
        i += d
    return divider[index]


def main():
    print(find_prime_number_from_order(10001))


if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print(f'Total Time = {t2 - t1} seconds')
