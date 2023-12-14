import logging

from src.effects import EffectFactory
from src.effects.normal import SetColor
from src.led_controller import LedControllerBase, create_led_controller
from src.networking import SocketHandler
from src.utils import ThreadedTask
from src.configuration import Configuration


def main():
    config = Configuration("config.ini")
    connection = SocketHandler(config.socket_host, config.socket_port)
    led_controller = create_led_controller(config.pixel_count)
    SetColor(config.init_color).apply(led_controller)

    connection.establish_connection()

    while True:
        try:
            update(connection, led_controller)
        except ValueError as e:
            logging.exception(e)


def update(connection: SocketHandler, led_controller: LedControllerBase):
    data = connection.receive_data()
    effect = EffectFactory.create_effect(data)
    thread = ThreadedTask(lambda: effect.apply(led_controller))
    thread.start()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
