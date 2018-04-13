import websockets


async def websocket_chat_message(message, ws='ws', address='localhost', port=8888):
    """ Используется для посылки сообщения в websocket"""
    uri = '{ws}://{address}:{port}'.format(ws=ws, address=address, port=port)
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
