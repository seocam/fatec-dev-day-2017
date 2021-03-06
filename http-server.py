
from socketserver import BaseRequestHandler, TCPServer

SESSION = {
    'logado': False,
}


def restrito():
    if not SESSION['logado']:
        return "403 Forbidden", "<h1>Acesso negado!</h1>"

    return "200 OK", "<h1>Acesso permitido! Bora la</h1>"


def index():
    return "200 OK", "<h1>Ola Mundo!</h1>"


def login():
    SESSION['logado'] = True
    return "200 OK", "<h1>Bem-vindo fulano</h1>"


def logout():
    SESSION['logado'] = False
    return "200 OK", "<h1>Ate logo</h1>"


class HTTPRequestHander(BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).decode('utf-8').strip()
        print(self.data)

        request_lines = self.data.split('\r\n')
        first_line = request_lines[0]
        verb, path, version = first_line.split(' ')

        if path == '/':
            status, response = index()
        elif path == '/restrito':
            status, response = restrito()
        elif path == '/sessao' and verb == 'POST':
            status, response = login()
        elif path == '/sessao' and verb == 'DELETE':
            status, response = logout()
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
