def collatz(n: int):
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        yield n
        if n == 1:
            break


if __name__ == "__main__":
    print(collatz(27))
