import requests
import re
import os
import json

print("PASO 1")

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

print("PASO 2")

r = requests.get(
    "https://www.amazon.es/gp/goldbox",
    headers={"User-Agent": "Mozilla/5.0"}
)

texto = r.text

productos = re.findall(
    r'"asin":"([^"]+)".*?"title":"([^"]+)".*?"link":"([^"]+)"',
    texto,
    re.DOTALL
)

print("PRODUCTOS:", len(productos))

asin, titulo, link = productos[0]

print("TITULO:", titulo)

url = f"https://www.amazon.es{link}?tag=verross-21"

boton = {
    "inline_keyboard": [[
        {
            "text": "🛒 Comprar en Amazon",
            "url": url
        }
    ]]
}

r = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": titulo,
        "reply_markup": json.dumps(boton)
    }
)

print("RESPUESTA TELEGRAM:")
print(r.text)
