import asyncio

from chat.youtube import youtube_client_chat


def add_youtube_task(channel, token):
    return asyncio.ensure_future(youtube_client_chat(channel, token))
