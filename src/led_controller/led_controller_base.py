import logging
from abc import ABC, abstractmethod

from src.colors import RgbColor


class LedControllerBase(ABC):
    def __init__(self, pixel_count: int):
        self.pixel_count = pixel_count
        logging.info("Initializing LedController with pixel count %i", pixel_count)

    @abstractmethod
    def set_color(self, index: int, color: RgbColor):
        """
        Sets the color of an LED at the given index
        :param index: the index of the LED to set the color for
        :param color: the color to set
        """
        pass

    @abstractmethod
    def get_color(self, index: int) -> RgbColor:
        """
        Returns the color of an LED at the given index
        :param index: the index of the LED to get the color for
        :return: the color of the LED at the given index
        """
        pass

    @abstractmethod
    def set_all_colors(self, color: RgbColor):
        """
        Sets the color of all LEDs
        :param color: the color to set
        """
        pass

    @abstractmethod
    def get_all_colors(self) -> list[RgbColor]:
        """:return: all the colors as list"""
        pass

    @abstractmethod
    def show(self):
        """Updates the LEDs"""
        pass
