from src.led_controller import LedControllerBase
from ..repeating_effect import RepeatingEffect


class RainbowWave(RepeatingEffect):
    def __init__(self, multiplier: float):
        self.multiplier = multiplier

    @classmethod
    def from_dict(cls, data: dict) -> 'RainbowWave':
        return RainbowWave(data.get("Multiplier"))

    def update(self, led_controller: LedControllerBase):
        raise NotImplementedError()
