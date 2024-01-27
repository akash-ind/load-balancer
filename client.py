import socket


class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        print(f"Listening on {(self.host, self.port)}")
        return self.sock.accept()

    def receive_data(self, conn):
        return conn.recv(1024)

    def send_data(self, conn, data):
        conn.sendall(data)

    def close(self, conn):
        conn.close()
        self.sock.close()

    def main(self):
        conn, addr = self.listen()
        try:
            data = self.receive_data(conn)
            print(f"Received client data: {data!r}")
            self.send_data(conn, data)
        finally:
            self.close(conn)


if __name__ == "__main__":
    client = Client(host="127.0.0.1", port=8999)
    client.main()
