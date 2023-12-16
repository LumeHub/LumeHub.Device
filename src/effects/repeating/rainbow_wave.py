import time

from src.led_controller import LedControllerBase
from ..repeating_effect import RepeatingEffect
from ...colors import RainbowCycleColor


class RainbowWave(RepeatingEffect):
    def __init__(self, multiplier: float):
        self.multiplier = multiplier

    @classmethod
    def from_dict(cls, data: dict) -> 'RainbowWave':
        return RainbowWave(data.get("Multiplier"))

    def update(self, led_controller: LedControllerBase):
        for j in range(256):
            for i in range(led_controller.pixel_count):
                led_controller.set_color(i, RainbowCycleColor(j, led_controller.pixel_count, self.multiplier, i))
            led_controller.show()
            time.sleep(0.005)
