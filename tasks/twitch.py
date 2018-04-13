import asyncio

from chat.twitch import twitch_client_chat


def add_twitch_task(username, channel, token):
    return asyncio.ensure_future(twitch_client_chat(username, channel, token))
