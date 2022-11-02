from typing import Iterator, Callable


class NumRange:
    def __default_func__(arg: int) -> int:
        return arg + 1

    # TODO: Figure out how to add another constructor with args:
    # (start: int, stop: int, step_func), in a way that doesn't
    # spoil type-hinting
    def __init__(self, stop: int, step_func: Callable[[int], int] = __default_func__):
        self.start = 0
        self.stop = stop
        self.step_func = step_func

    def __iter__(self) -> Iterator[int]:
        curr = self.start
        while curr < self.stop:
            yield curr
            curr = self.step_func(curr)


if __name__ == "__main__":
    for i in NumRange(10):
        print(i, end=" ")
    print()
    for i in NumRange(10, lambda x: x + 2):
        print(i, end=" ")
    print()
    for i in NumRange(100, lambda x: (x + 1) * 2):
        print(i, end=" ")
    print()
    print(list(NumRange(10)))
