from random import randint


class RgbColor(object):
    def __init__(self, red: int, green: int, blue: int):
        self.red = min(max(0, int(red)), 255)
        self.green = min(max(0, int(green)), 255)
        self.blue = min(max(0, int(blue)), 255)

    def to_tuple(self) -> tuple[int, int, int]:
        return int(self.red), int(self.green), int(self.blue)

    @classmethod
    def from_tuple(cls, color_tuple: tuple) -> 'RgbColor':
        return cls(*color_tuple)

    @classmethod
    def from_dict(cls, data: dict) -> 'RgbColor':
        return cls(int(data['Red']), int(data['Green']), int(data['Blue']))

    # <editor-fold desc="Operators">
    def __str__(self):
        return f"Red: {self.red}, Green: {self.green}, Blue: {self.blue}"

    def __hash__(self) -> hash:
        return hash(self.to_tuple())

    def __eq__(self, other: 'RgbColor') -> bool:
        if isinstance(other, RgbColor):
            return self.red == other.red and self.green == other.green and self.blue == other.blue
        return False

    def __add__(self, other: 'RgbColor') -> 'RgbColor':
        return RgbColor(self.red + other.red, self.green + other.green, self.blue + other.blue)

    def __sub__(self, other: 'RgbColor') -> 'RgbColor':
        return RgbColor(self.red - other.red, self.green - other.green, self.blue - other.blue)

    def __mul__(self, other: float) -> 'RgbColor':
        return RgbColor(int(self.red * other), int(self.green * other), int(self.blue * other))

    def __truediv__(self, other: int) -> 'RgbColor':
        return RgbColor(int(self.red / other), int(self.green / other), int(self.blue / other))

    def __abs__(self) -> 'RgbColor':
        return RgbColor(abs(self.red), abs(self.green), abs(self.blue))
    # </editor-fold>

    def distance(self, other) -> float:
        return max(abs(self.red - other.red), abs(self.green - other.green), abs(self.blue - other.blue))

    def is_color_similar(self, other, tolerance: int) -> bool:
        return (abs(self.red - other.red) <= tolerance
                and abs(self.green - other.green) <= tolerance
                and abs(self.blue - other.blue) <= tolerance)

    @staticmethod
    def random() -> 'RgbColor':
        return RgbColor(randint(0, 255), randint(0, 255), randint(0, 255))
