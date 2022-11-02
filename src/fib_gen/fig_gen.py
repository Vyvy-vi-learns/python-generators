from typing import Iterator


class FibGen:
    def __init__(self, length: int):
        self.num1 = 1
        self.num2 = 1
        self.length = length

    def __iter__(self) -> Iterator[int]:
        length = self.length
        while length > 0:
            length -= 1
            yield self.num1
            self.num1, self.num2 = self.num2, (self.num1 + self.num2)


if __name__ == "__main__":
    print(list(FibGen(20)))
