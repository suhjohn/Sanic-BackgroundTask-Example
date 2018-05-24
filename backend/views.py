import asyncio

from websockets import WebSocketCommonProtocol
from .tasks import consumers, producer

async def increment(request, websocket: WebSocketCommonProtocol):
    consumers.websockets.append(websocket)
    await websocket.send(str(producer.val))
    while producer.is_streaming:

        await asyncio.sleep(10)

