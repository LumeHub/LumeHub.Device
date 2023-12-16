from random import randint

from . import RgbColor


class RainbowColor(RgbColor):
    def __init__(self, position: int):
        """:param position: the position of the color in the rainbow 0 to 255"""
        if position < 85:
            super(RainbowColor, self).__init__(position * 3, 255 - position * 3, 0)
        elif position < 170:
            position -= 85
            super(RainbowColor, self).__init__(255 - position * 3, 0, position * 3)
        else:
            position -= 170
            super(RainbowColor, self).__init__(0, position * 3, 255 - position * 3)

    @classmethod
    def random(cls) -> 'RainbowColor':
        return cls(randint(0, 255))


class RainbowCycleColor(RainbowColor):
    def __init__(self, color_index: int, pixel_count: int, frequency_multiplier: float, pixel_index: int = 1):
        """:param color_index: the index of the color in the rainbow 0 to 255
        :param pixel_count: the number of pixels in the strip
        :param frequency_multiplier: the frequency multiplier to apply to the color cycle
        :param pixel_index: the index of the pixel in the strip"""
        super(RainbowCycleColor, self).__init__(((pixel_index * int(256 * frequency_multiplier)
                                                  // pixel_count) + color_index) % 256)
