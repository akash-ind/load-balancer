import asyncio
from conn_queue import ConnectionQueue


class Listener:

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 8283
        self.queue = ConnectionQueue.get_queue()

    async def accept_connection(self, reader, writer):
        asyncio.Task(self.queue.accept_connection((reader, writer)))

    async def start_server(self):
        server = await asyncio.start_server(self.accept_connection, self.host, self.port)

        async with server:
            await server.serve_forever()

