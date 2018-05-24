import asyncio

from websockets import ConnectionClosed
from .app import app

class Connection:
    def __init__(self):
        self.websockets = []


class StreamProducer:
    def __init__(self, consumers):
        self.val = 0
        self.consumers = consumers

    @property
    def is_streaming(self):
        return app.is_running

    async def stream_task(self):
        while True:
            await asyncio.sleep(1)
            self.val += 1
            for consumer in self.consumers:
                try:
                    await consumer.send(str(self.val))
                except ConnectionClosed:
                    self.consumers.remove(consumer)


consumers = Connection()
producer = StreamProducer(consumers.websockets)
