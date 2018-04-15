import asyncio
import websockets

from utils.parsemsg import parsemsg
from utils.chat import (
    websocket_chat_message,
    message_to_send
)


async def twitch_client_chat(username, channel, token):
    """Клиент чат на websocket"""
    async with websockets.connect('wss://irc-ws.chat.twitch.tv:443/irc') as websocket:
        await websocket.send('CAP REQ :twitch.tv/tags twitch.tv/commands twitch.tv/membership')
        await websocket.send('PASS ' + token)
        await websocket.send('NICK ' + username)
        await websocket.send('JOIN ' + '#' + channel)
        while True:
            try:
                # Получаем сообщения из websocket
                raw_msg = await websocket.recv()
                if raw_msg is None:
                    break
                try:
                    data = parsemsg(raw_msg)
                    display_name = data['display-name']
                    message = data['message']
                    if display_name and message:
                        await websocket_chat_message(
                            message_to_send(display_name, message, "twitch")
                        )
                except Exception as err:
                    pass
            except websockets.exceptions.ConnectionClosed as err:
                # Переподключение
                asyncio.sleep(0, loop=await twitch_client_chat(username, token, channel))
