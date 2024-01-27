import socket


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_data(self, data):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.host, self.port))
            sock.sendall(data)

            recv_data = b""

            while True:
                data = sock.recv(1024)
                if data:
                    recv_data += data
                else:
                    break

            return recv_data
