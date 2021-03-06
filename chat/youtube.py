import requests
import asyncio
import json

from api.youtube import (
    get_live_chat_id,
    get_live_stream_video_id_by_channel,
    request_chat_messages
)

from utils.chat import (
    websocket_chat_message,
    message_to_send
)


async def request_chat_messages_async(next_page_token, live_chat_id, token):
    try:
        body = request_chat_messages(next_page_token, live_chat_id, token)
        polling_interval_millis = body['pollingIntervalMillis']
        next_page_token_request = body['nextPageToken']
        items = body['items']

        for i in range(len(items)):
            message_raw = items[i]
            author_details = message_raw['authorDetails']
            display_name = author_details['displayName']
            snippet = message_raw['snippet']
            display_message = snippet['displayMessage']
            await websocket_chat_message(
                message_to_send(display_name, display_message, "youtube")
            )
        # Выставляем задержку на получение сообщений
        await asyncio.sleep(polling_interval_millis / 1000)
        # Делаем новый запрос с next_page_token
        await request_chat_messages_async(next_page_token_request, live_chat_id, token)
    except RecursionError:
        await request_chat_messages_async('', live_chat_id, token)


async def get_live_stream_video_id_by_channel_async(channel, token):
    try:
        video_id = get_live_stream_video_id_by_channel(channel, token)
        return video_id
    except Exception:
        asyncio.Task.current_task().stop()


async def youtube_client_chat(channel, token):
    # Получаем video_id стрима
    video_id = await get_live_stream_video_id_by_channel_async(channel, token)
    # Получаем live_chat_id для получения сообщений
    live_chat_id = get_live_chat_id(video_id, token)

    if live_chat_id:
        # Делаем запрос на получение сообщений
        await request_chat_messages_async('', live_chat_id, token)
