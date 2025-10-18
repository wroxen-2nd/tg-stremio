from flask import Flask

app = Flask(__name__)

@app.route('/health-status')
def hello_world():
    return 'Telegram stremio'
