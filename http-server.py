
from socketserver import BaseRequestHandler, TCPServer


class HTTPRequestHander(BaseRequestHandler):
    def handle(self):
        print('Oi! Eu cheguei até aqui! =)')


if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    TCPServer.allow_reuse_address = True
    with TCPServer((HOST, PORT), HTTPRequestHander) as server:
        server.serve_forever()
