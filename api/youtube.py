import requests
import json


def get_live_stream_video_id_by_channel(channel_id, token):
    """Получение video_id по channel_id"""
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    request_properties = {
        'part': 'snippet',
        'channelId': channel_id,
        'eventType': 'live',
        'type': 'video',
        'key': token
    }

    response = requests.get(search_url, request_properties)
    body = json.loads(response.content)
    items = body['items']
    try:
        video_id = items[0]['id']['videoId']
        return video_id
    except IndexError:
        # Данный канал не ведет онлайн трансляцию
        print("youtube broadcast offline")


def get_live_chat_id(video_id, token):
    """Получение live_chat_id по video_id"""
    videos_url = 'https://www.googleapis.com/youtube/v3/videos'

    request_params = {
        'id': video_id,
        'part': 'snippet,contentDetails,statistics,status,liveStreamingDetails',
        'key': token
    }

    response = requests.get(videos_url, request_params)
    body = json.loads(response.content)
    try:
        items = body['items'][0]
        live_streaming_details = items['liveStreamingDetails']
        active_live_chat_id = live_streaming_details['activeLiveChatId']
        return active_live_chat_id
    except KeyError as err:
        pass


def request_chat_messages(next_page_token, live_chat_id, token, max_results=200):
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
    return json.loads(response.content)
