from flask import Flask

app = Flask(__name__)

@app.route("/healthz")
def health_check():
    return "OK", 200

if __name__ == "__main__":
    # Bind to all interfaces and use port 8000
    app.run(host="0.0.0.0", port=8000)
