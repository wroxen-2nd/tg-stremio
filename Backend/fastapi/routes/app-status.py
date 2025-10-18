from fastapi import FastAPI

app = FastAPI()

@app.get("/health-status")
def health_status():
    return {"status": "ok", "message": "Telegram-Stremio server running 🚀"}
