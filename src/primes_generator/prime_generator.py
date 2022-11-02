from typing import Iterator

# TODO: Optimise if possible?


class PrimeRange:
    def next_prime(self, num: int) -> int:
        if num <= 1:
            return 2
        if num == 2:
            return 3

        while True:
            num += 2
            if num % 2 == 0 or num % 3 == 0:
                continue

            for i in range(5, int((num**0.5) + 1), 6):
                if num % i == 0 or num % (i + 2) == 0:
                    break
            else:
                break

        return num

    def __init__(self, stop: int):
        self.start = 2
        self.stop = stop

    def __iter__(self) -> Iterator[int]:
        curr = self.start
        while curr < self.stop:
            yield curr
            curr = self.next_prime(curr)


if __name__ == "__main__":
    print(list(PrimeRange(100)))
