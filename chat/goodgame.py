import asyncio
import websockets
import json

from api.goodgame import get_channel_id
from utils.chat import (
    websocket_chat_message,
    message_to_send
)

async def goodgame_client_chat(channel):
    """Клиент чат на websocket"""
    channel_id = get_channel_id(channel)
    async with websockets.connect('wss://chat-2.goodgame.ru/chat/websocket') as websocket:
        # https://github.com/GoodGame/API/blob/master/Chat/protocol.md
        # Заходим в чат по channel_id
        await websocket.send(json.dumps({"type": "join", "data": {"channel_id": channel_id, "hidden": False}}))
        while True:
            try:
                # Получаем сообщения
                raw_msg = await websocket.recv()
                if raw_msg is None:
                    break
                # Декодируем raw_msg
                message = json.loads(raw_msg)
                data = message['data']
                # Если type сообщения message
                if message['type'] == 'message':
                    username = data['user_name']
                    text = data['text']
                    await websocket_chat_message(
                        message_to_send(username, text, "goodgame")
                    )
            except websockets.exceptions.ConnectionClosed:
                # Переподключение к чату
                asyncio.sleep(0, loop=await goodgame_client_chat(channel))
