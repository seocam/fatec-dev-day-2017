
from socketserver import BaseRequestHandler, TCPServer


def index():
    return b"<h1>Ola Mundo!</h1>"


class HTTPRequestHander(BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode('utf-8').strip()
        print(self.data)

        request_lines = self.data.split('\r\n')
        first_line = request_lines[0]
        verb, path, version = first_line.split(' ')

        if path == '/':
            response = index()

        self.request.sendall(b"HTTP/1.1 200 OK\r\n")
        self.request.sendall(b"Content-Type: text/html\r\n\r\n")
        self.request.sendall(response)


if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    TCPServer.allow_reuse_address = True
    with TCPServer((HOST, PORT), HTTPRequestHander) as server:
        server.serve_forever()
