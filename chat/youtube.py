import requests
import asyncio
import json

from api.youtube import (
    get_live_chat_id,
    get_live_stream_video_id_by_channel
)

from utils.chat import websocket_chat_message


async def request_chat_messages(next_page_token, live_chat_id, token, max_results=200):
    """Запрос на получение сообщений из чата"""
    messages_url = 'https://www.googleapis.com/youtube/v3/liveChat/messages'

    request_properties = {
        "liveChatId": live_chat_id,
        "part": "snippet,id,authorDetails",
        "key": token,
        "maxResults": max_results,
        "pageToken": next_page_token
    }
    response = requests.get(messages_url, request_properties)
    body = json.loads(response.content)
    polling_interval_millis = body['pollingIntervalMillis']
    next_page_token_request = body['nextPageToken']
    items = body['items']

    for i in range(len(items)):
        message_raw = items[i]
        author_details = message_raw['authorDetails']
        display_name = author_details['displayName']
        snippet = message_raw['snippet']
        display_message = snippet['displayMessage']
        await websocket_chat_message("youtube - {name}: {message}".format(
            name=display_name,
            message=display_message
        ))
    # Выставляем задержку на получение сообщений
    await asyncio.sleep(polling_interval_millis / 1000)
    # Делаем новый запрос с next_page_token
    await request_chat_messages(next_page_token_request, live_chat_id, token)


async def youtube_client_chat(channel, token):
    # Получаем video_id стрима
    video_id = get_live_stream_video_id_by_channel(channel, token)
    # Получаем live_chat_id для получения сообщений
    live_chat_id = get_live_chat_id(video_id, token)

    if live_chat_id:
        # Делаем запрос на получение сообщений
        await request_chat_messages('', live_chat_id, token)
