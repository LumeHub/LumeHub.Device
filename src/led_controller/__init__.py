from os import name as os_name

from .led_controller_base import LedControllerBase

if os_name != 'nt':
    import board
    from .led_controller import LedController
else:
    from .console_led_controller import ConsoleLedController


def create_led_controller(pixel_count: int, brightness: float = 1.0) -> LedControllerBase:
    if os_name != 'nt':
        return LedController(pixel_count, brightness, board.MOSI, board.SCLK)
    else:
        return ConsoleLedController(pixel_count)
