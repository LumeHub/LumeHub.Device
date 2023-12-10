from abc import ABC, abstractmethod

from src.led_controller import LedControllerBase


class EffectBase(ABC):
    @abstractmethod
    def apply(self, led_controller: LedControllerBase):
        pass
