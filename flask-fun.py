
from flask import Flask, session
from flask_session import Session


app = Flask('Fun App')
app.config.update({
    'SESSION_TYPE': 'filesystem',
    'SESSION_COOKIE_DOMAIN': '.localhost',
})
Session(app)


@app.route("/")
def index():
    return "<h1>Hello World!</h1>"


@app.route("/restrito")
def restrito():
    if not session.get('logged_in'):
        return "<h1>Acesso negado!</h1>", 403

    return "<h1>Acesso permitido! Bora la</h1>"


@app.route("/sessao", methods=['POST'])
def login():
    session['logged_in'] = True
    return "<h1>Bem-vindo fulano</h1>"


@app.route("/sessao", methods=['DELETE'])
def logout():
    session['logged_in'] = False
    return "<h1>Ate logo</h1>"


if __name__ == '__main__':
    app.run()
