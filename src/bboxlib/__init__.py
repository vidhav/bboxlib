from math import inf


class BoundingBox:
    def __init__(
        self,
        left: float = inf,
        bottom: float = inf,
        right: float = -inf,
        top: float = -inf,
    ):
        self.left: float = left
        self.bottom: float = bottom
        self.right: float = right
        self.top: float = top

    @property
    def extent(self) -> list[float]:
        return [self.left, self.bottom, self.right, self.top]

    def extend(
        self,
        left: float,
        bottom: float,
        right: float,
        top: float,
    ):
        self.left = min(self.left, left)
        self.bottom = min(self.bottom, bottom)
        self.right = max(self.right, right)
        self.top = max(self.top, top)

    @property
    def west(self) -> float:
        return self.left

    @property
    def south(self) -> float:
        return self.bottom

    @property
    def east(self) -> float:
        return self.right

    @property
    def north(self) -> float:
        return self.top

    @property
    def minx(self) -> float:
        return self.left

    @property
    def miny(self) -> float:
        return self.bottom

    @property
    def maxx(self) -> float:
        return self.right

    @property
    def maxy(self) -> float:
        return self.top

    def __iter__(self):
        yield "left", self.left
        yield "bottom", self.bottom
        yield "right", self.right
        yield "top", self.top

    def __repr__(self) -> str:
        return f"BoundingBox({self.left}, {self.bottom}, {self.right}, {self.top})"
