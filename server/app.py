from tornado.ioloop import IOLoop
from tornado.web import Application, url

from server.websocket import EchoWebSocket


def server_load_app():
    settings = {}

    return Application(handlers=[
        url(r'/', EchoWebSocket)
    ], **settings)


if __name__ == '__main__':
    app = server_load_app()
    app.listen(8888)
    IOLoop.start()