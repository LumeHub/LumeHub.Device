from abc import abstractmethod

from .effect_base import EffectBase
from src.led_controller import LedControllerBase
from src.utils import ThreadedTask


class RepeatingEffect(EffectBase):
    thread: ThreadedTask

    def apply(self, led_controller: LedControllerBase):
        self.thread = ThreadedTask(lambda: self._loop(led_controller))
        self.thread.start()

    def _loop(self, led_controller: LedControllerBase):
        while True:
            self.update(led_controller)

    def stop(self):
        self.thread.kill()

    @abstractmethod
    def update(self, led_controller: LedControllerBase):
        pass
