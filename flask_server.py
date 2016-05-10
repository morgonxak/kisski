from flask.app import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Привет, Киски!"


def start_server():
    app.run(host='0.0.0.0', port='')
