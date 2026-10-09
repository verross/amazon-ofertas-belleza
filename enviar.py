import requests
import re
import os
import json

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Leer ASIN ya publicados
try:
    with open("publicados.txt", "r") as f:
        publicados = f.read().splitlines()
except:
    publicados = []

# Leer Amazon Goldbox
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

for asin, titulo, link in productos:

    # Saltar productos ya publicados
    if asin in publicados:
        continue

    url = f"https://www.amazon.es{link}?tag=verross-21"

    boton = {
        "inline_keyboard": [[
            {
                "text": "🛒 Comprar en Amazon",
                "url": url
            }
        ]]
    }

    mensaje = f"""🎁 OFERTA AMAZON 🎁

{titulo}
"""
     respuesta = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": mensaje,
            "reply_markup": json.dumps(boton)
        }
    )

    print("Publicado:", asin)
    print(respuesta.text)

    # Guardar ASIN
    with open("publicados.txt", "a") as f:
        f.write(asin + "\n")

    break
``


print("RESPUESTA TELEGRAM:")
print(r.text)
