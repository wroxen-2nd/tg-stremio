from flask import Flask

app = Flask(__name__)
@app.route('/healthstatus')
def hello_world():
    return 'Stremio'
if __name__ == "__main__":
    app.run()
