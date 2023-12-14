import configparser

from src.colors import RgbColor


class Configuration:
    def __init__(self, config_file_path: str):
        config = configparser.ConfigParser()
        config.read(config_file_path)

        self.socket_host = config['socket']['host']
        self.socket_port = int(config['socket']['port'])

        self.pixel_count = int(config['led_controller']['pixel_count'])
        self.init_color = RgbColor(int(config['led_controller.init_color']['red']),
                                   int(config['led_controller.init_color']['green']),
                                   int(config['led_controller.init_color']['blue']))
