import json
import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio

class TimeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            await self.send(text_data=json.dumps({'time': now}))
            await asyncio.sleep(1)