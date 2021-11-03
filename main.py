from app.kudos import Kudos
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return '''<h1>Bem vindo ao conversor de kudos</h1>
    <p>Para testar o projeto navegue até a url http://127.0.0.1:5000/kudos </p>
    <p>Em seguida, acrescente a quantia de kudos como parâmetro direto na url e.g http://127.0.0.1:5000/kudos/40
    '''


@app.route('/kudos/<int:kudopoints>')
def kudos(kudopoints):
    kudos_cli = Kudos()
    return kudos_cli.output(kudopoints)


app.run()
