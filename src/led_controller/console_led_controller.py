from colr import color as colr_color
from numpy import empty
from src.colors import RgbColor
from . import LedControllerBase


class ConsoleLedController(LedControllerBase):
    def __init__(self, pixel_count: int):
        super().__init__(pixel_count)
        self.leds = empty(pixel_count, dtype=tuple)
        self.set_all_colors(RgbColor(0, 0, 0))

    def set_color(self, index: int, color: RgbColor):
        self.leds[index] = color.to_tuple()

    # noinspection PyTypeChecker
    def get_color(self, index: int) -> RgbColor:
        return RgbColor.from_tuple(self.leds[index])

    def set_all_colors(self, color: RgbColor):
        self.leds.fill(color.to_tuple())

    def get_all_colors(self) -> list[RgbColor]:
        colors = []
        for i in range(len(self.leds)):
            color = self.get_color(i)
            colors.append(color)
        return colors

    def show(self):
        for i in range(len(self.leds)):
            color = self.get_color(i)
            print(colr_color('▇', fore=color.to_tuple(), back=color.to_tuple()), end="")
        print("")
