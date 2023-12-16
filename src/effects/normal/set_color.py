from src.colors import RgbColor
from ..effect_base import EffectBase
from src.led_controller import LedControllerBase


class SetColor(EffectBase):
    def __init__(self, color: RgbColor):
        self.color = color

    @classmethod
    def from_dict(cls, data: dict) -> 'SetColor':
        return cls(RgbColor.from_dict(data.get("Color")))

    def apply(self, led_controller: LedControllerBase):
        led_controller.set_all_colors(self.color)
        led_controller.show()
