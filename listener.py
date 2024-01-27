import socket


class Listener:

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8283
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        print(f"Listening on {(self.host, self.port)}")
        self.conn, addr = self.sock.accept()
        print(f"Accepted connection from {addr}")

    def get_data(self):
        return self.conn.recv(1024)

    def send_data(self, data):
        self.conn.sendall(data)

    def close(self):
        self.conn.close()
        self.sock.close()


