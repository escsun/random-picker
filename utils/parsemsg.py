def parsemsg(text):
    """Twitch IRC parser"""
    try:
        meta, msgtype, channel, message = text.split(' ', maxsplit=3)
        meta = dict(tag.split('=') for tag in meta.split(';'))
        # Заносим message в словарь
        # Разделяем строку "#channel :message"
        # Удаляем \r\n с помощью rstrip
        meta['message'] = message.split(' :')[1].rstrip()
        return meta
    except Exception:
        pass
    return False
