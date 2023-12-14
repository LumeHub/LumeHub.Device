import logging
import jsonpickle

from json import JSONDecodeError, loads as json_loads
from socket import socket, AF_INET, SOCK_STREAM


class SocketHandler:
    connection: socket
    address: str

    def __init__(self, host: str, port: int, packet_size: int = 1024):
        self.host = host
        self.port = port
        self.packet_size = packet_size

    def establish_connection(self):
        server_socket = socket(AF_INET, SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        logging.info("Server listening on port %i", self.port)
        server_socket.listen(1)
        self.connection, self.address = server_socket.accept()
        logging.info("Connection established")

    def _handle_data_traffic(self, func):
        try:
            return func()
        except (ConnectionResetError, BrokenPipeError, JSONDecodeError):
            logging.warning("Connection reset by host. Reconnecting...")
            self.connection.close()
            self.establish_connection()
            return self._handle_data_traffic(func)

    def send_data(self, data: dict):
        self._handle_data_traffic(lambda: self._send_data_internal(data))

    def _send_data_internal(self, data: dict):
        json_data = jsonpickle.encode(data, unpicklable=False)
        self.connection.send(json_data.encode())

    def receive_data(self):
        return self._handle_data_traffic(lambda: self._receive_data_internal())

    def _receive_data_internal(self):
        json_str = self.connection.recv(self.packet_size)
        return json_loads(json_str)
