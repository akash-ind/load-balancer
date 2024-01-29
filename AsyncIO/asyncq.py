import os
import asyncio
import random
import time
from asyncio import Queue


def get_random_string(size: int = 5):
    return os.urandom(size).hex()


async def sleep_random_time(name=None):
    time = random.randint(1, 5)
    if name:
        print(f"{name} sleeping for {time} seconds")
    await asyncio.sleep(time)


async def producer(queue: Queue, name=None):
    n = random.randint(1, 5)

    for _ in range(n):
        await sleep_random_time(name)
        item = get_random_string()
        await queue.put((item, name))
        print(f"{name} added {item} to queue")


async def consumer(queue: Queue, name=None):
    while True:
        await sleep_random_time(name)
        item, producer_name = await queue.get()

        print(f"Got {item} from {producer_name} at consumer {name}")

        queue.task_done()


async def main(ncon: int, nprod: int):
    q = Queue()
    producers = [asyncio.create_task(producer(q, f"producer-{i}")) for i in range(nprod)]
    consumers = [asyncio.create_task(consumer(q, f"consumer-{i}")) for i in range(ncon)]
    produced_time = time.perf_counter()

    await asyncio.gather(*producers)

    print(f"Total time required to produce - {time.perf_counter() - produced_time}")
    await q.join()

    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    ncon = 10
    nprod = 2
    s = time.perf_counter()
    asyncio.run(main(ncon, nprod))
    print(f"Took time {time.perf_counter() - s} Seconds")