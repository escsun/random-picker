import requests
import untangle


def get_channel_id(channel):
    try:
        # Делаем запрос по имени канала и получаем xml
        response = requests.get('https://goodgame.ru/api/getggchannelstatus?id={channel_name}'.format(
            channel_name=channel))
        try:
            # Парсим xml ответ response.text
            xml = untangle.parse(response.text)
            # root > stream > id
            channel_id = xml.root.stream['id']
            # Возвращаем channel_id
            return channel_id
        except AttributeError as err:
            print("Channel not found")
    except requests.exceptions.RequestException as err:
        print("Request exception: ", err)
