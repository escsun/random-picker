from tasks.twitch import add_twitch_task
from tasks.youtube import add_youtube_task
from tasks.goodgame import add_goodgame_task

from definitions import (
    YOUTUBE_OPTIONS,
    TWITCH_OPTIONS,
    GOODGAME_OPTIONS
)


def tasks_load_app():
    """Запуск задач"""
    goodgame_properties = {
        "channel": GOODGAME_OPTIONS["channel"]
    }

    youtube_properties = {
        "channel": YOUTUBE_OPTIONS["channel"],
        "token": YOUTUBE_OPTIONS["token"]
    }

    twitch_properties = {
        "channel": TWITCH_OPTIONS["channel"],
        "username": TWITCH_OPTIONS["username"],
        "token": TWITCH_OPTIONS["token"]
    }

    if goodgame_properties["channel"]:
        add_goodgame_task(
            channel=goodgame_properties["channel"]
        )
        print("goodgame task added")

    if youtube_properties["channel"] and youtube_properties["token"]:
        add_youtube_task(
            channel=youtube_properties["channel"],
            token=youtube_properties["token"]
        )
        print('youtube task added')

    if twitch_properties["username"] and twitch_properties["channel"] and twitch_properties["token"]:
        add_twitch_task(
            username=twitch_properties["username"],
            channel=twitch_properties["channel"],
            token=twitch_properties["token"]
        )
        print("twitch task added")
