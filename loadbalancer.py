import asyncio
from server import Server
from conn_queue import ConnectionQueue


class LoadBalancer:
    def __init__(self):
        self.server_pool = []
        self.connection_queue = ConnectionQueue.get_queue()

    def add_server(self, server):
        self.server_pool.append(server)

    def remove_server(self, server):
        self.server_pool.remove(server)

    def get_server(self):
        return self.server_pool[0]

    @staticmethod
    async def get_data(reader):
        data = await reader.read(-1)
        return data

    @staticmethod
    def send_to_server(server, data):
        received_data = server.send_data(data)



    async def main(self):
        while True:
            reader, writer = await self.connection_queue.get_connection()


if __name__ == "__main__":
    load_balancer = LoadBalancer()
    server = Server(host="127.0.0.1", port=8999)
    load_balancer.add_server(server)
    load_balancer.main()
