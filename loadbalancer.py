from listener import Listener
from server import Server


class LoadBalancer:
    def __init__(self):
        self.server_pool = []

    def add_server(self, server):
        self.server_pool.append(server)

    def remove_server(self, server):
        self.server_pool.remove(server)

    def get_server(self):
        return self.server_pool[0]

    def main(self):
        listener = Listener()
        try:
            data = listener.get_data()

            if not self.server_pool:
                raise Exception("No server available")

            server = self.get_server()
            received_data = server.send_data(data)

            print(received_data)

            listener.send_data(received_data)
        finally:
            listener.close()


if __name__ == "__main__":
    load_balancer = LoadBalancer()
    server = Server(host="127.0.0.1", port=8999)
    load_balancer.add_server(server)
    load_balancer.main()


