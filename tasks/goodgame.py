import asyncio

from chat.goodgame import goodgame_client_chat


def add_goodgame_task(channel):
    return asyncio.ensure_future(goodgame_client_chat(channel))
