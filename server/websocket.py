from tornado.websocket import WebSocketHandler

active_clients = set()


class EchoWebSocket(WebSocketHandler):

    def open(self):
        active_clients.add(self)

    def check_origin(self, origin):
        return True

    def data_received(self, chunk):
        pass

    def on_message(self, message):
        print(message)
        for client in active_clients:
            client.write_message(message)

    def on_close(self):
        active_clients.remove(self)

