import adafruit_ws2801
import board

from src.colors import RgbColor
from . import LedControllerBase


class LedController(LedControllerBase):
    def __init__(self, pixel_count: int, brightness: float, o_data: board, o_clock: board):
        super().__init__(pixel_count)
        self.leds = adafruit_ws2801.WS2801(o_clock, o_data, pixel_count, brightness=brightness, auto_write=False)

    def set_color(self, index: int, color: RgbColor):
        self.leds[index] = color.to_tuple()

    def get_color(self, index: int) -> RgbColor:
        index = min(index, self.pixel_count - 1)
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
        self.leds.show()
