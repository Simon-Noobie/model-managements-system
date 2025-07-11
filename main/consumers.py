import json
import datetime
from urllib.parse import parse_qs
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
from asgiref.sync import sync_to_async


class TimeConsumer(AsyncWebsocketConsumer):
    from urllib.parse import parse_qs

    async def connect(self):
        from rest_framework.authtoken.models import Token
        query_string = self.scope["query_string"].decode()
        print("🔍 WebSocket Query String:", query_string)

        params = parse_qs(query_string)
        token_key = params.get("token", [None])[0]
        print("🔑 Extracted Token:", token_key)

        if not token_key:
            print("❌ No token provided. Closing socket.")
            await self.close()
            return

        try:
            token = await sync_to_async(Token.objects.get)(key=token_key)
            user = await sync_to_async(lambda: token.user)()
            self.scope["user"] = user
            print(f"✅ Authenticated user: {user.username}")
        except Token.DoesNotExist:
            print("❌ Invalid token. Closing socket.")
            await self.close()
            return

        await self.accept()
        print("✅ WebSocket connection accepted.")
        while True:
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            await self.send(text_data=json.dumps({'time': now}))
            await asyncio.sleep(1)