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
        divider = False
        while i < x:
            if x % i == 0:
                divider = True
            i += 1
        if not divider:
            break
    return x


def main():
    print(find_prime_number_from_order(10001))


if __name__ == "__main__":
    main()
