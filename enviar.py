import requests
import re
import os
import json

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

coincidencias = re.findall(r'/dp/([A-Z0-9]{10})', r.text)

asin = coincidencias[0]

url = f"https://www.amazon.es/dp/{asin}?tag=verross-21"

boton = {
    "inline_keyboard": [
        [
            {
                "text": "🛒 Comprar en Amazon",
                "url": url
            }
        ]
    ]
}

