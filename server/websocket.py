from tornado.websocket import WebSocketHandler


class EchoWebSocket(WebSocketHandler):

    def data_received(self, chunk):
        pass

    def on_message(self, message):
        # TODO delete print message latter
        print(message)
        self.write_message(message)
