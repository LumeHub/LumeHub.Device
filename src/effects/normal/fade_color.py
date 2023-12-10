from src.colors import RgbColor
from src.effects.effect_base import EffectBase
from src.led_controller import LedControllerBase


class FadeColor(EffectBase):
    def __init__(self, color: RgbColor):
        self.color = color

    @classmethod
    def from_dict(cls, data: dict) -> 'FadeColor':
        return FadeColor(RgbColor.from_dict(data.get("Color")))

    def apply(self, led_controller: LedControllerBase):
        raise NotImplementedError()
