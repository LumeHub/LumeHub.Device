from src.effects.effect_base import EffectBase
from src.led_controller import LedControllerBase


class RainbowWave(EffectBase):
    def __init__(self, multiplier: float):
        self.multiplier = multiplier

    @classmethod
    def from_dict(cls, data: dict) -> 'RainbowWave':
        return RainbowWave(data.get("Multiplier"))

    def apply(self, led_controller: LedControllerBase):
        raise NotImplementedError()
