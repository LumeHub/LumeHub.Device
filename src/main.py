import logging

from src.configuration import Configuration
from src.effects import EffectFactory, EffectBase, RepeatingEffect
from src.effects.normal import SetColor
from src.led_controller import LedControllerBase, create_led_controller
from src.networking import SocketHandler


def main():
    config = Configuration("config.ini")
    connection = SocketHandler(config.socket_host, config.socket_port)
    led_controller = create_led_controller(config.pixel_count)
    previous_effect = SetColor(config.init_color)
    previous_effect.apply(led_controller)

    connection.establish_connection()
    while True:
        try:
            previous_effect = update(connection, led_controller, previous_effect)
        except ValueError as e:
            logging.exception(e)


def update(connection: SocketHandler, led_controller: LedControllerBase, previous_effect: EffectBase):
    data = connection.receive_data()
    if isinstance(previous_effect, RepeatingEffect):
        previous_effect.stop()
    effect = EffectFactory.create_effect(data)
    effect.apply(led_controller)
    return effect


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
