from typing import Optional, Iterator


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"


class PointList:
    def __init__(self, size: int = 0, init_value: Optional[Point] = None):
        self.size = size
        self.len = 0
        self.items = list()
        for _ in range(size):
            self.items.append(init_value)

    def __iter__(self) -> Iterator[Point | None]:
        i = 0
        while i < self.len:
            yield self.items[i]
            i += 1

    def __repr__(self) -> str:
        i = 0
        repr_str = "["
        while i < self.len - 2:
            repr_str += self.items[i].__repr__() + ", "
            i += 1
        repr_str += self.items[i].__repr__() + "]"
        return repr_str

    def append(self, item: Point):
        if self.len == self.size:
            raise OverflowError(
                f"Can't insert more elements. PointList is at full capacity of {self.size} elements."
            )
        self.items[self.len] = item
        self.len += 1


if __name__ == "__main__":
    points = PointList(4)
    print(list(points))
    points.append(Point(2, 3))
    points.append(Point(3, 5))
    points.append(Point(4, 5))
    print(points)
    print(list(points))
