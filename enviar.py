import requests
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

r = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": "PRUEBA TELEGRAM"
    }
)

print(r.text
