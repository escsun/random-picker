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
    except IndexError as err:
        # Данный канал не ведет онлайн трансляцию
        print("Broadcast offline")


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
        print("Key error:", err)
