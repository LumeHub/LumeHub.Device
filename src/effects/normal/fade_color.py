import time

from src.colors import RgbColor, RgbColorUtils
from ..effect_base import EffectBase
from src.led_controller import LedControllerBase


class FadeColor(EffectBase):
    def __init__(self, color: RgbColor):
        self.color = color

    @classmethod
    def from_dict(cls, data: dict) -> 'FadeColor':
        return cls(RgbColor.from_dict(data.get("Color")))

    def apply(self, led_controller: LedControllerBase):
        current_color = led_controller.get_color(0)
        for color in RgbColorUtils.interpolate_colors(current_color, self.color, 12):
            led_controller.set_all_colors(color)
            led_controller.show()
            time.sleep(0.01)
