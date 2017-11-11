
from socketserver import BaseRequestHandler, TCPServer


def index():
    return "<h1>Ola Mundo!</h1>"


class HTTPRequestHander(BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).decode('utf-8').strip()
        print(self.data)

        request_lines = self.data.split('\r\n')
        first_line = request_lines[0]
        verb, path, version = first_line.split(' ')
        status = '200 OK'

        if path == '/':
            response = index()
        else:
            status = '404 Not Found'
            response = '<h1>Pagina nao encontrada!</h1>'

        self.request.sendall("HTTP/1.1 {}\r\n".format(status).encode('utf-8'))
        self.request.sendall(b"Content-Type: text/html\r\n\r\n")
        self.request.sendall(response.encode('utf-8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 8000
    TCPServer.allow_reuse_address = True
    with TCPServer((HOST, PORT), HTTPRequestHander) as server:
        server.serve_forever()
