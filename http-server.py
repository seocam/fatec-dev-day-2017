
from socketserver import BaseRequestHandler, TCPServer


class HTTPRequestHander(BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(self.data.decode('utf-8'))

        self.request.sendall(b"HTTP/1.1 200 OK\r\n")
        self.request.sendall(b"Content-Type: text/html\r\n\r\n")
        self.request.sendall(b"<h1>Ola Mundo!</h1>")


if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    TCPServer.allow_reuse_address = True
    with TCPServer((HOST, PORT), HTTPRequestHander) as server:
        server.serve_forever()
