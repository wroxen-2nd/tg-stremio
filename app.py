from flask import Flask

app = Flask(__name__)

@app.route('/healthcheck')
def healthcheck():
    return "OK", 200

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it’s accessible externally
    # Use port 8000 (Render default) or your preferred port
    app.run(host="0.0.0.0", port=8000)
