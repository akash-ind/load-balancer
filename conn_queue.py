import asyncio


class ConnectionQueue:
    """
    Not thread safe
    """

    QUEUE = None

    def __init__(self):
        self.queue = asyncio.Queue()

    @staticmethod
    def get_queue():
        if not ConnectionQueue.QUEUE:
            ConnectionQueue.QUEUE = ConnectionQueue()
        return ConnectionQueue.QUEUE

    async def accept_connection(self, reader, writer):
        asyncio.Task(self.queue.put((reader, writer)))

    async def get_connection(self):
        return await self.queue.get()

    async def close_connection(self):
        self.queue.task_done()
